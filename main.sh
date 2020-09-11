pip install pipenv
@echo off
mkdir src\credentials
@(
echo credentials = {
echo     "email_username" : "",
echo     "email_password" : "",
echo     "postgresql_name" : "",
echo     "postgresql_username" : "",
echo     "postgresql_password" : "",
echo     "postgresql_host" : "",
echo     "postgresql_port" : "",
echo     "secret_key" : "",
echo }
) >src\credentials\credentials.py
@echo Enter credentials in  src\credentials\credentials.py
read -p "Press any key to resume ..."
start notepad src\credentials\credentials.py
read -p "Press any key to resume ..."
python -m pipenv sync
python -m pipenv install
python -m pipenv run python src\manage.py makemigrations
python -m pipenv run python src\manage.py migrate
python -m pipenv run python src\manage.py collectstatic
@echo Enter following details for user
python -m pipenv run python src\manage.py createsuperuser
read -p "Press any key to resume ..."
python -m pipenv run python src\manage.py makemigrations
python -m pipenv run python src\manage.py migrate
python -m pipenv run python src\manage.py runserver
read -p "Press any key to resume ..."
