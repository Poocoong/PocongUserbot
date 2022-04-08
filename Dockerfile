FROM poocongonlen/poconguserbot:buster

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm

RUN git clone -b main https://github.com/poocoong/PoocongUserbot /home/pooconguserbot/ \
    && chmod 777 /home/pooconguserbot \
    && mkdir /home/pooconguserbot/bin/

WORKDIR /home/pooconguserbot/

CMD [ "bash", "start" ]
