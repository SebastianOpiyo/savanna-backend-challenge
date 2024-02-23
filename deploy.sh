#!/usr/bin/env bash
set -e

ENV_TYPE=prod
BUILD_TAG=savannah-$ENV_TYPE-$BUILD_NUMBER
REGISTRY=ghcr.io/SebastianOpiyo

echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

docker build -f ./docker/docker_files/Dockerfile . -t savannah/django-rest-api
docker tag savannah/django-rest-api $REGISTRY/django-rest-api:$BUILD_TAG
docker push $REGISTRY/django-rest-api:$BUILD_TAG

docker build -f ./docker/celery-worker/Dockerfile . -t savannah/celery-worker
docker tag savannah/celery-worker $REGISTRY/savannah-celery-worker:$BUILD_TAG
docker push $REGISTRY/savannah-celery-worker:$BUILD_TAG

docker build -f ./docker/celery-flower/Dockerfile . -t savannah/celery-flower
docker tag savannah/celery-flower $REGISTRY/savannah-celery-flower:$BUILD_TAG
docker push $REGISTRY/savannah-celery-flower:$BUILD_TAG