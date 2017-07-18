====
RAD City Website
====

## Prerequisites
- Python 3


##Setup

1. Create a virtual environment with `pyvenv env` (unless you're installing it outside the folder, please name the environment folder "env")
2. `pip install -r requirements`
3. Create a new settings file in `pdxrad/settings/`, you can copy the `template.py` file*
4. In your project's root, type the following:

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Running locally

1. Comment out Storage Settings
2.

After that you should be able to view the site in the browser at `http://localhost:8000`

*If you're running locally, name it `local.py`, otherwise you'll need to create an `environment.py` file in root and change the `DJANGO_SETTINGS_MODULE` variable


```
. env/bin/activate
python manage.py runserver
```
