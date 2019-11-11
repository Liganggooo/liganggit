FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
#RUN apk update \
#  Pillow dependencies\
#  && apk add freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev openssh --no-cache

WORKDIR /app
RUN python -m pip install --upgrade pip -i https://pypi.doubanio.com/simple/
RUN apk add --update --no-cache jpeg-dev zlib-dev g++ gcc
RUN pip install pillow -i https://pypi.doubanio.com/simple/
COPY ./requirments.txt /app/requirments.txt
RUN pip install -r requirments.txt -i https://pypi.doubanio.com/simple/
COPY . /app

COPY ./compose/production/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh
