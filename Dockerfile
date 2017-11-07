FROM python:3.6-alpine3.6

LABEL maintainer="Brian Rotich <brianrotych@gmail.com>"

COPY . /app
WORKDIR /app/viewer


RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]
