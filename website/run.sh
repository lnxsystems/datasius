#!/bin/sh 


MYDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd)"
echo $MYDIR
PARENTDIR="$(dirname $MYDIR)"
WEBSITEDIR="${PARENTDIR}/website"
MANAGEPY="${PARENTDIR}/website/manage.py"

python3 $MANAGEPY collectstatic --noinput

echo "Entering website directory: $WEBSITEDIR"
cd $WEBSITEDIR
gunicorn --access-logfile -  --error-logfile - -b 0.0.0.0:8008 website.wsgi
