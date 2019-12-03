test:
	pytest -vv --ignore tests/test_api.py

test-http-real:
	pytest -vv tests/test_api.py

lint:
	black cryptowatch tests examples
