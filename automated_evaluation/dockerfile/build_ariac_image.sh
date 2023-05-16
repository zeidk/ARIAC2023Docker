#!/bin/bash -x
set -e

# Uncoment this line to rebuild without cache
#DOCKER_ARGS="--no-cache"

set -x

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo " Build image: ariac-image"

DOCKER_ARGS="--no-cache"
USERID=`id -u $USER`
if [[ ${USERID} != 0 ]]; then
  DOCKER_ARGS="--build-arg USERID=${USERID}"
fi

docker build --force-rm ${DOCKER_ARGS} --tag ariac-image-1.4:latest $DIR