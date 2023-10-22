#!/bin/sh

set -e

if [ $DEV != "true" ]; then
    echo "Triggered Build Logic"
    python manage.py wait_for_db
    python manage.py collectstatic --noinput
    python manage.py migrate

    uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
fi