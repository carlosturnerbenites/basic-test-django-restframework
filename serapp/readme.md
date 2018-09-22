virtualenv env
source env/bin/activate

pip3 install Django==2.1.1
python3 -m django --version
django-admin startproject mysite
python3 manage.py runserver

python3 manage.py startapp api
move api/ to apps/

pip3 install djangorestframework

python3 manage.py migrate

python3 manage.py createsuperuser --email carlosturnerbenites@gmail.com --username carlosturnerbenites

# pass: secret

pip3 install coreapi

