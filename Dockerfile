FROM python:3.6-alpine3.6

LABEL maintainer="Brian Rotich <brianrotych@gmail.com>"

# add curl for healtcheck
RUN apk add --no-cache curl

# build dependacies needed for building grpc clients
RUN apk add --virtual build-dependencies --no-cache \
        python3-dev \
        gcc g++ \
        libc-dev
# add python dependacies
COPY viewer/requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
# remove build dependacies
RUN apk del build-dependencies

COPY . /app
WORKDIR /app/

EXPOSE 5000

CMD ["python", "/app/viewer/app.py"]
