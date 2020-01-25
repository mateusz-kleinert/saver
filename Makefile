init:
	pip install -r requirements.txt

format:
	black .

mypy:
	mypy saver/

test:
	pytest tests/

.PHONY: init format mypy test
