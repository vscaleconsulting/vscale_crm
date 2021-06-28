release: python manage.py makemigrations; python manage.py migrate; python manage.py shell < leads/processes.py
web: gunicorn vscale_crm.wsgi:application
