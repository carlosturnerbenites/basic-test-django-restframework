# Basic Test with Django RestFramework

virtualenv env
source env/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py createsuperuser --email [email] --username [username]

python3 manage.py runserver
