FROM node:18 AS build

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .

FROM node:18-slim

WORKDIR /usr/src/app

COPY --from=build /usr/src/app .

EXPOSE 3000
CMD [ "npm", "start" ]
