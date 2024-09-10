# How to run the challenge

This challenge requires:

- A Google Cloud Project with:
  - One Cloud Function v1
  - One service account with Logger write and read access
- An LLM server with Ollama and `Llama3.1:8b`
  - The LLM server is available in the `llm_server` folder

First, create a `.env` file by copying the `.env.example` file.

## Google Cloud

First create a project on Google Cloud then go to IAM and create a new service account:

- [Google Cloud Console IAM service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
- After creation click on the new service account name, then click on `Keys` and `ADD Key` and download in JSON format
- Save the JSON file as `google-cloud-service-account.json`
- Go to the [IAM page](https://console.cloud.google.com/iam-admin/iam), select your service account and `Grand Access` to `Logs Writer` and `Logs Viewer`

Now create a new Cloud Function:

- [Google Cloud Console Cloud Functions](https://console.cloud.google.com/functions/add)
  - Environment: Cloud Run function (1st gen)
  - Choose the region and name you want
  - Runtime: Python 3.12

From the code editor in the Google Cloud Console, copy the following files to it and edit the `Entry point` to be `is_admin`

- `google-cloud-service-account.json`
- `is_admin_cloud_function.py` to the content of the `main.py` file
- `requirements.txt`

Once you have the Cloud Function created, copy the URL and add it to the `.env` file.

## LLM Server

The LLM server is available in the `llm_server` folder. To run it, run the following command:

```bash
cd llm_server
docker compose up -d
```

If your system doesn't have an Nvidia GPU, you can remove this section of the `docker-compose.yml` file to run on cpu:

```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: 1
          capabilities: [gpu]
```

Once the server is running, add the URL  (`"http://localhost:5001"`) to the `.env` file.

## Flask

To run the Flask server, run the following commands:

```bash
docker build -t helpful-assistant .
docker run -p 5000:5000 -d helful-assistant:latest
```
