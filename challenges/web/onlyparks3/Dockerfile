FROM node:20

WORKDIR /app

COPY ./package* .
COPY ./node_modules node_modules
COPY ./schema.prisma .

COPY ./index.ts .
COPY ./initdb.ts .
COPY ./static static

RUN npm install
RUN npm prune

RUN npm install -g ts-node

ENV DATABASE_URL file:./database.db
ENTRYPOINT [ "npm", "run", "start:docker" ]