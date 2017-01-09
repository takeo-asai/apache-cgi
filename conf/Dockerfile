FROM httpd:2.4.25-alpine

COPY conf/httpd.conf /usr/local/apache2/conf/httpd.conf

RUN apk update && apk add --update openssl \
        && apk add ca-certificates wget curl \
        && update-ca-certificates \
        && apk add make libc-dev gcc perl-dev alpine-sdk \
        && curl -L https://cpanmin.us | perl -  App::cpanminus \
        && cpanm Carton
