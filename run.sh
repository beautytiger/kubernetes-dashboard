#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail
shopt -s lastpipe

DIR=$(cd $(dirname "${BASH_SOURCE[0]}") >/dev/null 2>&1 && pwd)
cd $DIR

python manage.py makemigrations
python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000
