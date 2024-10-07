#!/bin/sh

set -e

if [ $DEV != "true" ]; then
    python manage.py wait_for_db
    python manage.py collectstatic --noinput
    python manage.py migrate

    uwsgi --http-socket 0.0.0.0:9090 --workers 4 --master --enable-threads --module app.wsgi
fi
