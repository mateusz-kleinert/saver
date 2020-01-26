init:
	pip install -r requirements.txt
	python utils/generate_enums.py saver/enums/enums.py

format:
	black saver/ utils/

mypy:
	mypy --config-file mypy.ini saver/ utils/

test:
	pytest tests/

.PHONY: init format mypy test
