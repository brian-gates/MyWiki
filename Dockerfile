FROM python:2

WORKDIR /usr/src/app

COPY . .

RUN pip install bottle

CMD [ "python", "./myWiki.py" ]
