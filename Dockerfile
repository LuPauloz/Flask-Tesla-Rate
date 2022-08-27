FROM alpine:3.16.2


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1


WORKDIR /app
EXPOSE 8000
COPY . .
RUN apk update && apk add  --no-cache --virtual .build-deps postgresql-dev python3-dev curl \
    g++ musl-dev libffi-dev shadow sudo git
RUN python3 -m ensurepip --upgrade
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install "poetry==1.1"
RUN poetry config virtualenvs.create false
RUN poetry install