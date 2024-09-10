default: none

none:
	@echo "Please specify a target to build"

poetry_export:
	poetry export -f requirements.txt --without-hashes --output requirements.txt
	poetry export -f requirements.txt --without-hashes --with llm --output llm_server/requirements.txt
