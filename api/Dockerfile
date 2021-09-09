FROM python:3.9-alpine

ARG PYTHON_VERSION="python3.9"

ENV PYTHONUNBUFFERED="1" \
    PYTHONPATH="/usr/local/lib/${PYTHON_VERSION}/site-packages:/usr/lib/${PYTHON_VERSION}/site-packages"

RUN set -ex; \
    # install prerequisites
    apk add --no-cache \
        git \
        # fftcgtool deps
        g++ \
        jpeg-dev \
        zlib-dev \
    ; \
    # Twistd Webserver
    pip3 --no-cache-dir install \
        Twisted \
    ;

COPY . /usr/src/fftcgtool_api

RUN set -ex; \
    pip3 --no-cache-dir install --use-feature=in-tree-build \
        /usr/src/fftcgtool_api \
    ;

EXPOSE 8080
CMD [ "twistd", "-n", "web", "--listen", "tcp:8080", "--wsgi", "fftcgtool_api.wsgi.app" ]
