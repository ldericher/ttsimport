FROM antonapetrov/uvicorn-gunicorn:python3.9-alpine3.13

RUN set -ex; \
    # fftcgtool prerequisites
    apk add --no-cache \
        git \
        # fftcgtool deps
        g++ \
        jpeg-dev \
        zlib-dev \
    ;

ENV PRODUCTION_MODE="True" \
    APP_MODULE="ttsimport.main:app"

COPY . /usr/src/ttsimport

RUN set -ex; \
    pip3 --no-cache-dir install --use-feature=in-tree-build \
        /usr/src/ttsimport \
    ;
