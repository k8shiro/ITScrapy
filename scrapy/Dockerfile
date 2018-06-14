FROM python:3.6

RUN mkdir /scrapy
COPY ./ /scrapy
WORKDIR /scrapy
RUN pip install -r requirements.txt

CMD ["ping", "localhost"]
