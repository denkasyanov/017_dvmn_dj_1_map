#!/bin/sh

wait_db_up () {
    echo "Waiting for database $1..."

    while ! nc -z "$1" "$2"; do
      sleep 0.1
    done

    echo "Database $1 started."
}



if [ "$DATABASE" = "postgres" ]
then
    for DB in db
    do
        wait_db_up $DB 5432
    done
fi

python manage.py collectstatic --noinput

# python manage.py flush --no-input
python manage.py migrate

exec "$@"
