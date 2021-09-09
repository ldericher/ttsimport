FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN set -ex; \
    # install prerequisites
    apk add --no-cache \
        git \
        # fftcgtool deps
        g++ \
        jpeg-dev \
        zlib-dev \
        # uwsgi
        uwsgi \
        uwsgi-python3 \
    ;

COPY . /usr/src/fftcgtool-api

RUN set -ex; \
    pip3 --use-feature=in-tree-build install /usr/src/fftcgtool-api
