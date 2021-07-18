#!/bin/sh

python3 var_get.py
export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0
docker build -t dv_bot_image .
docker run -d --rm --name dv_bot_con dv_bot_image
sh reset_original_vars.sh
rm -rf reset_original_vars.sh
