FROM nginx:1.17.1


RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./compose/production/nginx/sources.list /etc/apt/

RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/production/nginx/ligangblog.conf /etc/nginx/conf.d/ligangblog.conf
