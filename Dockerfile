############
# build ui #
############

FROM node:lts-alpine AS build-ui

# some dir for our code
WORKDIR /app

# install dependencies
COPY ui/package*.json ui/yarn*.lock ./
RUN  yarn --production=false

# copy code
COPY ui .
RUN  yarn build


##############
# webservice #
##############

FROM antonapetrov/uvicorn-gunicorn:python3.9-alpine3.13 AS production

RUN set -ex; \
  # fftcgtool prerequisites
  apk add --no-cache \
  git \
  # fftcgtool deps
  g++ \
  jpeg-dev \
  zlib-dev \
  ;

# env setup
ENV \
  PRODUCTION_MODE="True" \
  APP_MODULE="ttsimport.main:app"

# install API
COPY api /usr/src/ttsimport
RUN set -ex; \
  pip3 --no-cache-dir install --use-feature=in-tree-build \
  /usr/src/ttsimport \
  ;

# install UI
COPY --from=build-ui /app/dist /html
