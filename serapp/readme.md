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


python3 manage.py makemigrations series
python3 manage.py sqlmigrate series 0001


python3 manage.py shell
>>> from apps.series.models import Genre, Serie
In [2]: g = Genre(name="Seinen")
In [3]: g.save()
In [7]: import datetime
s = Serie(name="Mushishi", rate=10, airing_at=datetime.datetime.now())
s.genres.add(g)
