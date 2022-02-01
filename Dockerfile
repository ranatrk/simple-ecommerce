FROM ubuntu:18.04
      ENV FLASK_APP app.py
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

COPY /app/* /app/
COPY /app/data/* /app/data/
COPY /app/tests/* /app/tests/



