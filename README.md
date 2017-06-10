# python-sandbox

## Apps
1. Groceries
2. Polls - [Django Tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)
3. Blog - [Django Girls Tutorial](https://tutorial.djangogirls.org/en/django_installation/)

## Requirements
- This repo uses python 2.7,
- Django 1.10


## Step One: Set up and activate Virtual Environment
- install virtualenv, but add pipy.python as a trusted host b/c of firewall settings: `pip install --trusted-host pypi.python.org virtualenv`
- activate virtual environment: `source pyenv/bin/activate` where `pyenv` is the name of the virutal environment.

## Step Two: Install Django
- Upgrade pip
	- `pip install --trusted-host pypi.python.org --upgrade pip` (may or may not be necessary)
- Install Django
	- `pip install --trusted-host pypi.python.org django~=1.10.0 ` || `pip install django=~1.10.0`
- Create Django project
	- `django-admin startproject sitename . `


## Step Three: Update Settings in `sitename/settings.py`
1. Timezone ('America/Chicago' will work for Central)-
	`TIME_ZONE='America/Chicago'`
1. Add path for static files (CSS,JS, etc.)
	```
	STATIC_URL = '/static'
	STATIC_ROOT = 'os.path.join(BASE_DIR, 'static')
	```
1. other settings to modify may include: ALLOWED_HOSTS, DATABASES, etc.


## Step Four: Create Django App
1. Create Django App
	- `python manage.py startapp appname`
2. Add app to project in INSTALLED_APPS array in `sitename/settings.py`
```
INSTALLED APPS= [
	'django.contrib.admin',
	[...]
	'appname',
]
```
## Step Five: Breathe Life into the App!
### Models: `appname/models.py`
1. import necessaries
	```python
	from django.db import models
	from django.utils import timezone
	```
1. define model:
	```python
	class Modelname(models.Model):
		user = models.ForeignKey('auth.User')
		string = models.CharField(max_length=200)
		text = models.TexField()
		created_date = models.DateTimeField(default = timezone.now)
		action_date = models.DateTimeField(blank=True, null=True)

		def action(self):
			self.action_date = timezone.now()
			self.save()

		def __str__(self):
			return self.string
	```
1. [more field types](https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types)

1. create the migration: `python manage.py makemigrations`
1. run the migration: `python manage.py migrate`
1. register the model within `appname/admin.py` if you want to be able to manage it via the admin panel
	```python
	from django.contrib import admin
	from .models import Modelname

	admin.site.register(Modelname)

	```

### DjangoAdmin
1. create superuser: `python manage.py createsuperuser`

### URLs
1. Create app url file: `appname/urls.py`
- import url configurations, app views:
	```python
	#appname/urls.py
	
	from django.conf.urls import url
	from . import views
	
	
	urlpatterns = [
		url(r'^models/(?P<pk>\d+)/$', ClassViewModel.as_view(), name='route_name'), 	
	]

	```
### Views
### Templates
### Materialize
### Gitignore
```git
	*.pyc
	*~
	__pycache__
	pyenv (or whatever you name your virtualenv)
	db.sqlite3
	/static
	.DS_Store
```

# Reference

### Reference: `python manage.py` Commands
- Server
	- `python manage.py runserver`
- Migrations
	- `python manage.py makemigrations`
	- `python manage.py migrate`
- Shell
	- `python manage.py shell`
- Django
	- `django-admin startproject sitename .`
	- `python manage.py startapp appname`
	- `python manage.py createsuperuser`

### Structure of a Django Directory
- Run: `django-admin startproject sitename . `
```
projectname
|____ manage.py
|____ sitename
      settings.py
      urls.py
      wsgi.py
      __init__.py
```
- Run: `python manage.py startapp appname`
```
projectname
├── appname
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── .gitignore (* need to create this manually)
└── sitename
  ├── __init__.py
  ├── settings.py
  ├── urls.py
  └── wsgi.py
```

## Shell Stuff
1. start shell `python manage.py shell`
1. import necessaries: 
	```
	>> import django
	>> django.setup()
	>> from django.utils import timezone
	
	```
1. import models:
	```
	>>> from app.models import Modelname
	```
1. list objects:
	```
	>>> Modelname.objects.all()
	```
1. filter objects:
	```
	>>> Modelname.objects.get(field=value)
	>>> Modelname.objects.filter(id=1)
	```

	```

