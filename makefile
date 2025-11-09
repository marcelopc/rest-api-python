install:
	pip install -r requirements.txt

start-dev:
	uvicorn main:app --reload

migrate:
		alembic revision --autogenerate -m "$(msg)"

upgrade:
	alembic upgrade head