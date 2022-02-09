# !/bin/bash

pendings=`python3 manage.py showmigrations | grep '\[ \]' | wc -l`
if [ $pendings -ge 1 ]
then
    python3 manage.py migrate
    python3 manage.py seed reports --number 15
fi
