FROM node:20

WORKDIR /code

COPY package*.json /code/
RUN npm cache clean --force
RUN rm -rf node_modules package-lock.json
RUN npm install react-scripts@latest
RUN npm install react-dev-utils
RUN npm install

COPY . /code/
EXPOSE 3000
CMD ["npm", "start"]
