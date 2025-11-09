install:
	pip install -r requirements.txt

start-dev:
	uvicorn main:app --reload