#!/bin/sh

set -e

echo "$DEV thee dev var val"
if [ $DEV != "true" ]; then
    echo "Triggered Build Logic"
    python manage.py wait_for_db
    python manage.py collectstatic --noinput
    python manage.py migrate

    uwsgi --socket :9090 --workers 4 --master --enable-threads --module app.wsgi
fi