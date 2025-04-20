release: python manage.py setup_project && python manage.py collectstatic
web: gunicorn UserManagement.wsgi:application