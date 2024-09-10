# LLM Server

This llm server is required to run the llm model. It is a simple flask server that listens for POST requests. The request must contain the following keys in the json body:

- `validation_password`: Hardcoded password to ensure that only the intended application can access the server.
- `message`: The message that the model should generate a response for.

The server is running `Ollama` on port `11434` and a Flask app on port `5001`.

The LLM model running on the server is `llama3.1:8b` with a custom system prompt.
