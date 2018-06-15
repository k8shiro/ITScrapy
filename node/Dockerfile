FROM node:9

ENV HTTP_PROXY ${HTTP_PROXY}
ENV HTTPS_PROXY ${HTTPS_PROXY}
ENV http_proxy ${http_proxy}
ENV https_proxy ${https_proxy}


EXPOSE 3000

RUN mkdir /root/node
COPY ./ /root/node/
WORKDIR /root/node/app


RUN npm install
RUN cd client; npm install
CMD ["npm", "run", "dev"]
#CMD ["ping", "localhost"]
