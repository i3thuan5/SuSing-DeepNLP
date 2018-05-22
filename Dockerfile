FROM i3thuan5/deepnlp
MAINTAINER sih4sing5hong5

WORKDIR /usr/local/deepnlp/deepnlp/pos
COPY data/tw.conf data/tw.conf
RUN cat data/tw.conf >> data/models.conf

COPY data/tw/train.txt data/tw/train.txt
COPY data/tw/dev.txt data/tw/dev.txt
COPY data/tw/test.txt data/tw/test.txt

RUN python3 pos_model.py tw

WORKDIR /usr/local/deepnlp
RUN pip3 install Flask gunicorn
COPY 標詞性.py 標詞性.py
EXPOSE 5000

