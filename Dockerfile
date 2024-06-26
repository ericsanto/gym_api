FROM python:3.12

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get upgrade -y

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . ./

RUN chmod +x entrypoint.sh

CMD [ "./entrypoint.sh" ]
