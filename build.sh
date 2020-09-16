#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

DIR=$(cd $(dirname "${BASH_SOURCE[0]}") >/dev/null 2>&1 && pwd)
cd $DIR

image='harbor.beautytiger.com/docker.io/k8sdashboard:0.1.0'
docker build -t "$image" .
docker push "$image"
#docker run --rm -it -p80:8000 "$image"
