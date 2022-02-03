FROM ubuntu:18.04
      ENV FLASK_APP server.py
      ENV FLASK_RUN_HOST 0.0.0.0
      ENV LC_ALL C.UTF-8
      ENV LANG C.UTF-8
RUN apt-get update && apt-get install -y \
    python3 python3-pip
RUN pip3 install flask pytest pytest-dependency requests
EXPOSE 5000
RUN mkdir /app
RUN mkdir /app/data
RUN mkdir /app/tests

COPY /app /app/
COPY /app/catalogue /app/catalogue/
COPY /app/catalogue/data /app/catalogue/data/
COPY /app/tests /app/tests/
COPY /app/__init__.py /app/
COPY /app/tests/__init__.py /app/tests



