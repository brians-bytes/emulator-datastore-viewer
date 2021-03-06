FROM python:3.6-alpine3.6

LABEL maintainer="Brian Rotich <brianrotych@gmail.com>"

# add curl for healtcheck
RUN apk add --no-cache curl git

# build dependacies needed for building grpc clients
RUN apk add --virtual build-dependencies --no-cache \
        python3-dev \
        gcc g++ \
        libc-dev \
        linux-headers

# add python dependacies
WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt

# remove build dependacies
RUN apk del build-dependencies

COPY . /app
WORKDIR /app

EXPOSE 5000

CMD ["python", "/app/app.py"]
