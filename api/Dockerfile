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
    ;

COPY . /usr/src/ttsimport

RUN set -ex; \
    pip3 --no-cache-dir install --use-feature=in-tree-build \
        /usr/src/ttsimport \
    ;

EXPOSE 8000
CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "8000", "--factory", "ttsimport.main:main" ]
