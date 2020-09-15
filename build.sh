#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

DIR=$(cd $(dirname "${BASH_SOURCE[0]}") >/dev/null 2>&1 && pwd)
cd $DIR

image='k8sdashboard:demo'
docker build -t "$image" .
docker run --rm -it -p80:8000 "$image"
