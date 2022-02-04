FROM ubuntu:18.04
      ENV FLASK_APP ecommerce_app.py
      ENV FLASK_RUN_HOST 0.0.0.0
      ENV LC_ALL C.UTF-8
      ENV LANG C.UTF-8
RUN apt-get update && apt-get install -y \
    python3 python3-pip
RUN pip3 install flask pytest pytest-dependency requests
EXPOSE 5000
RUN mkdir /ecommerce_app
RUN mkdir /ecommerce_app/data
RUN mkdir /ecommerce_app/tests

COPY /ecommerce_app /ecommerce_app/
COPY /ecommerce_app/catalogue /ecommerce_app/catalogue/
COPY /ecommerce_app/catalogue/data /ecommerce_app/catalogue/data/
COPY /ecommerce_app/tests /ecommerce_app/tests/
COPY /ecommerce_app/__init__.py /ecommerce_app/
COPY /ecommerce_app/tests/__init__.py /ecommerce_app/tests



