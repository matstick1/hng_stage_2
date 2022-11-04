python manage.py migrate
gunicorn stage_1.wsgi:application