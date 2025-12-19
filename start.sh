python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn voterid.wsgi:application --bind 0.0.0.0:$PORT