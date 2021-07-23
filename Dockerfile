FROM python:3-alpine3.12

WORKDIR /usr/src/app

RUN apk update && apk add gcc libc-dev
COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/. .

CMD [ "python", "./main.py" ]
