FROM ubuntu:18.04

EXPOSE 8080

ENV DATABASE_NAME=""
ENV DATABASE_USER=""
ENV DATABASE_PASSWORD=""
ENV DATABASE_HOST=""
ENV DATABASE_PORT=""
ENV PYTHONPATH="/app"

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y python3.7 python3.7-dev python3-pip default-libmysqlclient-dev libssl-dev build-essential libgnutls30 && \
    python3.7 -m pip install mysqlclient gunicorn && \
    apt-get install -y mysql-server && \
    mkdir app

COPY ./app /app
WORKDIR /app

RUN python3.7 -m pip install -r requirements.txt && \
    python3.7 manage.py collectstatic --noinput

# Use gunicorn
CMD ["gunicorn", "-w", "4", "-b", ":8080", "<%= name %>.wsgi"]