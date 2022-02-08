# !/bin/bash

python manage.py migrate
python manage.py seed reports --number 15