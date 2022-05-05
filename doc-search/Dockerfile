# Making build faster : nulti stages, cache the pip install layesr which does not ifently changes
# Making docker image smaller: use another base image
FROM python:3.10-alpine as base
COPY src /app
COPY requirements.txt /app

RUN pip install -r app/requirements.txt

FROM base as prod
COPY samples /data

WORKDIR /app
EXPOSE 8080

ENTRYPOINT [ "python3" ]
CMD [ "__init__.py", "/data" ]