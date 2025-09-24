#!/bin/bash

# Wait for DB
echo "Waiting for MySQL..."
while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
  sleep 1
done
echo "MySQL started"

# Migrate and collect static
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Start Gunicorn
gunicorn lms.wsgi:application --bind 0.0.0.0:8000
