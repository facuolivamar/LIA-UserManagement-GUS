release: python UserManagement/manage.py setup_project && python UserManagement/manage.py collectstatic
web: gunicorn UserManagement.wsgi:application