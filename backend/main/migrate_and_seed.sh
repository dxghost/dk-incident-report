# !/bin/bash

pendings=`python3 manage.py showmigrations | grep '\[ \]' | wc -l`
if [ $pendings -ge 1 ]
then
    python3 manage.py migrate
    python3 manage.py createsuperuser --email $DJANGO_SUPERUSER_EMAIL --noinput
    python3 register_tasks.py
fi
