poetry:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
