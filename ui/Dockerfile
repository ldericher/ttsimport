FROM node:lts-alpine as build

# some dir for our code
WORKDIR /app

# install dependencies
COPY package*.json yarn*.lock ./
RUN  yarn --production=false

# copy code
COPY . .
RUN  yarn build


FROM nginx:stable-alpine AS production
COPY production/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/dist /usr/share/nginx/html