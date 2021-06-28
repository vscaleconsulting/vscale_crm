release: python manage.py makemigrations; python manage.py migrate

web: gunicorn vscale_crm.wsgi:application
python manage.py shell < leads/processes.py