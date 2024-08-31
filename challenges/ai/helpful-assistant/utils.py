import os
import time
from typing import List, Tuple

import google.oauth2.id_token
import requests
from dotenv import load_dotenv
from flask import json
from google.auth.transport import requests as google_auth_requests
from google.cloud import logging

load_dotenv()

LOG_COUNT = 10
CLIENT = logging.Client(project="unitedctf-2024")
LOG_EXPLORER_FILTER = """
resource.type = "cloud_function"
resource.labels.function_name = "function-1"
resource.labels.region = "northamerica-northeast1"
severity=(DEFAULT OR INFO)
labels.instance_id={INSTANCE_ID}
textPayload=~"{USER_UUID}.*"
"""
# ^ I needed to prefix the user_uuid to ensure each user gets their own logs
# I hope people don't lose too much time on this

GOOGLE_CLOUD_FUNCTION_URL = os.environ.get("GOOGLE_CLOUD_FUNCTION_URL")


def call_cloud_function(
    user_guess_password: str, user_comment: str, user_uuid: str
) -> Tuple[str, int]:
    """Function that invokes a cloud function."""

    data = {
        "user_comment": user_comment,
        "user_guess_password": user_guess_password,
        "user_uuid": user_uuid,
    }
    request = google_auth_requests.Request()
    audience = GOOGLE_CLOUD_FUNCTION_URL
    token = google.oauth2.id_token.fetch_id_token(request, audience)

    r = requests.post(
        audience,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        data=json.dumps(data),
        timeout=10,
    )

    instance_id = r.text
    status_code = r.status_code

    return instance_id, status_code


def get_logs(instance_id: str, user_uuid: str) -> str:
    """Get logs from the cloud function."""

    # Prepare filter to only get logs from the cloud function
    filter_ = LOG_EXPLORER_FILTER.format(INSTANCE_ID=instance_id, USER_UUID=user_uuid)

    # Get logs with DEFAULT or INFO severity
    entries = CLIENT.list_entries(
        filter_=filter_,
        max_results=LOG_COUNT,
        order_by=logging.DESCENDING,
        page_token=None,
    )

    data = {}
    for entry in entries:
        log_data = {}
        log_data["severity"] = entry.severity
        log_data["message"] = entry.payload
        data[str(entry.timestamp)] = log_data

    return data
