init:
	pip install -r requirements.txt

mypy:
	mypy saver/

test:
	pytest tests/

.PHONY: init mypy test
