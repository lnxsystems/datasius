#!/bin/sh 


MYDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd)"
echo $MYDIR
PARENTDIR="$(dirname $MYDIR)"
FRONTENDDIR="${PARENTDIR}/frontend"
MANAGEPY="${PARENTDIR}/frontend/manage.py"

python3 $MANAGEPY collectstatic --noinput

echo "Entering frontend directory: $FRONTENDDIR"
cd $FRONTENDDIR
gunicorn --access-logfile -  --error-logfile - -b 0.0.0.0:8008 frontend.wsgi
