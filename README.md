# python-sandbox

## Grocery List

## Polls - Django Tutorial

## Blog - Django Girls Tutorial

## Django Takeaways
- This repo uses python 2.7, django 1.10


### Step One: Set up and activate Virtual Environment
- install virtualenv, but add pipy.python as a trusted host b/c of firewall settings: `pip install --trusted-host pypi.python.org virtualenv`
- activate virtual environment: `source pyenv/bin/activate` where `pyenv` is the name of the virutal environment.

### Step Two: Install Django
- Upgrade pip
	- `pip install --trusted-host pypi.python.org --upgrade pip` (may or may not be necessary)
- Install Django
	- `pip install --trusted-host pypi.python.org django~=1.10.0 ` || `pip install django=~1.10.0`
- Create Django project
	- `django-admin startproject sitename . `


### Step Three: Update Settings in `sitename/settings.py`
1. Timezone ('America/Chicago' will work for Central)-
`TIME_ZONE='America/Chicago'`
1. Add path for static files (CSS,JS, etc.)
	```
	STATIC_URL = '/static'
	STATIC_ROOT = 'os.path.join(BASE_DIR, 'static')
	```
1. other settings to modify may include: ALLOWED_HOSTS, DATABASES, etc.


### Step Four: Create Django App
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

### Structure of a Django Directory
	Run: `django-admin startproject sitename . `

		```
		projectname
		|____ manage.py
		|____ sitename
		      settings.py
		      urls.py
		      wsgi.py
		      __init__.py
		```
	Run: `python manage.py startapp appname`
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
		└── sitename
		    ├── __init__.py
		    ├── settings.py
		    ├── urls.py
		    └── wsgi.py
		```
