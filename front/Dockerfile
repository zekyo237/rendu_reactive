FROM node:lts-alpine as build-stage
WORKDIR /front
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# étape de production
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /front/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]