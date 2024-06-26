#!/bin/bash
set -e

TAG_NAME=kiipy-docs-build:latest

# ensure the output folder is created
mkdir -p ../site

# build the latest image
docker build -t "${TAG_NAME}" .

docker run --rm -v "${PWD}/..:/app" "${TAG_NAME}"
