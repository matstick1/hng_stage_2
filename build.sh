python manage.py migrate
gunicorn stage_2.wsgi:application