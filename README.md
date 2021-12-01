для запуска необходимо:

создать файл .env в который прописать:
SECRET_KEY = you_secret_key
DB_NAME  = db_name
DB_USER  = db_user
DB_PASSWORD = db_password
DB_HOSTNAME = db_hostname
DB_PORT = db_port

установитмь зависимости:
pipenv install -d --pre

выполнить миграции:
./manage.py migrate

запустить:
./manage.py runserver
