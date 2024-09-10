import os
import random
import uuid
from typing import Dict

import flask
import requests

from const import (
    ADMIN_PASSWORD,
    ADMIN_PASSWORD_FLAG,
    CHAT_V2_PASSPHRASE,
    FLAG_01_VALIDATION_PASSWORD,
    FLAG_02_VALIDATION_PASSWORD,
)
from utils import call_cloud_function, get_logs

app = flask.Flask(__name__, static_url_path="/static")
app.secret_key = uuid.uuid4().hex

OLLAMA_HOST = os.environ.get("OLLAMA_HOST")


@app.route("/", methods=["GET"])
def home():
    """home route."""
    flask.session.clear()

    return flask.render_template("home.html")


@app.route("/login", methods=["GET"])
def login_get():
    """Login route."""
    user_uuid = str(uuid.uuid4())
    flask.session["user_uuid"] = user_uuid

    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    """Login route."""
    user_guess_password = flask.request.form["user_guess_password"]
    user_comment = flask.request.form["user_comment"]
    user_uuid = flask.session.get("user_uuid")

    # check that the user_uuid is set
    if not user_uuid:
        return flask.redirect("/")

    # check that user_guess_password and user_comment are set
    if not user_guess_password or not user_comment:
        return flask.redirect("/login"), 400

    # Call the cloud function to see if the user is admin
    instance_id, status_code = call_cloud_function(
        user_guess_password, user_comment, user_uuid
    )

    # set session variables
    flask.session["user_comment"] = user_comment
    flask.session["instance_id"] = instance_id
    flask.session["user_guess_password"] = user_guess_password

    if status_code == 200:
        return "Oh an admin!", status_code

    data = {
        "user_comment": flask.session["user_comment"],
    }
    return flask.jsonify(data), status_code


@app.route("/logs", methods=["GET"])
def logs():
    instance_id = flask.session.get("instance_id")
    user_uuid = flask.session.get("user_uuid")

    logs: Dict[str, str] = get_logs(instance_id, user_uuid)

    return flask.jsonify(logs)


@app.route("/admin", methods=["GET"])
def admin():
    user_guess_password = flask.session.get("user_guess_password")
    if user_guess_password == ADMIN_PASSWORD:
        return flask.render_template("admin.html", flag=ADMIN_PASSWORD_FLAG)
    return flask.render_template("no.html")


def get_greeting_message():
    """Invoke LLM to get greeting message."""
    return "Hello, I am your helpful assistant. How can I help you?"


@app.route("/send_message", methods=["POST"])
def send_message():

    access_passphrase = flask.session.get("access_passphrase", "")
    message = flask.request.form["message"]

    # Hardcoded password use to authenticate the request to the llm server
    validation_password = (
        FLAG_01_VALIDATION_PASSWORD
        if access_passphrase != CHAT_V2_PASSPHRASE
        else FLAG_02_VALIDATION_PASSWORD
    )

    # Send the message to the llm server
    response = requests.post(
        f"{OLLAMA_HOST}/send_message",
        json={"validation_password": validation_password, "message": message},
    )

    answer = response.content.decode("utf-8")

    if "flag" in answer and validation_password == FLAG_02_VALIDATION_PASSWORD:
        answer = "".join(random.sample(answer, len(answer)))

    if response.status_code != 200:
        answer = "Sorry, the LLM is down. Please try again later. If the issue persist, contact Hannibal119 on Discord."

    flask.session["answer"] = answer
    flask.session["message"] = message

    return flask.redirect("/chat")


@app.route("/request_access", methods=["GET"])
def request_access():
    access_passphrase = flask.session.get("access_passphrase", "")

    return flask.render_template(
        "request_access.html", access_passphrase=access_passphrase
    )


@app.route("/request_access", methods=["POST"])
def request_access_post():
    access_passphrase = flask.request.form.get("access_passphrase", "")
    flask.session["access_passphrase"] = access_passphrase

    if access_passphrase == CHAT_V2_PASSPHRASE:
        return flask.redirect("/chat")
    return flask.redirect("/request_access")


@app.route("/chat", methods=["GET"])
def chat():

    access_passphrase = flask.session.get("access_passphrase", "")
    is_v2 = access_passphrase == CHAT_V2_PASSPHRASE
    message = flask.session.get("message")
    answer = flask.session.get("answer")
    return flask.render_template(
        "chat.html",
        get_greeting_message=get_greeting_message,
        user_message=message,
        llm_message=answer,
        is_v2=is_v2
    )


@app.route("/cloud_function_src", methods=["GET"])
def src():
    return flask.send_from_directory(".", "is_admin_cloud_function.py")


# create a robot.txt file
@app.route("/robots.txt", methods=["GET"])
def robots():
    return flask.send_from_directory(".", "robots.txt")


if __name__ == "__main__":
    app.run(debug=False)
