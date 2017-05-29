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
- `pip install --trusted-host pypi.python.org --upgrade pip` (may or may not be necessary)
- `pip install --trusted-host pypi.python.org django~=1.10.0 ` || `pip install django=~1.10.0`

### Structure of a Django Directory
```
projectname
|____ manage.py
|____ sitename
      settings.py
      urls.py
      wsgi.py
      __init__.py
```
