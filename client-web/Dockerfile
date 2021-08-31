FROM node:16

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install -g http-server

RUN npm install

COPY . .

RUN node ./node_modules/esbuild/install.js

RUN npm run build

VOLUME [ "/usrc/src/app/public" ]

EXPOSE 5000