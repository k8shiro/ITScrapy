FROM python:3.6-alpine3.6

RUN apk update
RUN apk add --update curl gcc g++ py-lxml libffi-dev openssl-dev libxml2-dev libxslt-dev \
    && rm -rf /var/cache/apk/*

RUN mkdir /scrapy
COPY ./ /scrapy
WORKDIR /scrapy

RUN pip install  --no-cache-dir -r requirements.txt

COPY ./cron /var/spool/cron/crontabs/root 

CMD ["crond", "-l", "2", "-f"]
