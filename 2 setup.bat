@echo off
mkdir src\credentials
@(
echo credentials = {
echo     "email_username" : "optional",
echo     "email_password" : "optional",
echo     "postgresql_name" : "optional",
echo     "postgresql_username" : "optional",
echo     "postgresql_password" : "optional",
echo     "postgresql_host" : "optional",
echo     "postgresql_port" : "optional",
echo     "secret_key" : "required",
echo     "consumer_key" : "required",
echo     "consumer_secret" : "required",
echo     "access_token" : "required",
echo     "access_token_secret" : "required",
echo }
) >src\credentials\credentials.py
@echo Enter credentials in  src\credentials\credentials.py
pause
start notepad src\credentials\credentials.py
pause
python -m pipenv sync
python -m pipenv install
python -m pipenv run python src\manage.py makemigrations
python -m pipenv run python src\manage.py migrate
python -m pipenv run python src\manage.py collectstatic
@echo Enter following details for user
python -m pipenv run python src\manage.py createsuperuser
pause
