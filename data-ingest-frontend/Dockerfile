# Stage 0, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.15
#Copy ci-dashboard-dist
COPY /dist/data-ingest-frontend/ /usr/share/nginx/html
#Copy default nginx configuration
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf
