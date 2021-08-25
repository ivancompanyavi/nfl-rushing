FROM node:16

RUN mkdir -p /usr/share/app

WORKDIR /usr/share/app

COPY . /usr/share/app
RUN npm install

EXPOSE 8000

CMD ["npm run serve"]