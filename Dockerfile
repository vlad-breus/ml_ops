FROM ubuntu

LABEL classifier_version="0.12"
LABEL owner="Vlad"

# install libraries and packages
RUN apt-get update && apt-get install -y \
python3-pip \
python3-dev \
python3-numpy \
python3-scipy \
python3-pip

RUN pip install scikit-learn flask-restful

# copy model and service code from current directory
COPY . /model

# expose the port for API
EXPOSE 8100

# set environment variables
ENV ml_debug_level=1
ENV environment PRODUCTION

# run the api, replace later with Flask app running
CMD ["flask", "run"]
