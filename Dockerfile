FROM ubuntu

LABEL classifier_version="0.15"
LABEL owner="Vlad"

# install libraries and packages
RUN apt-get update && apt-get install -y \
python3-pip \
python3-dev

# copy model and service code from current directory
COPY . /model
WORKDIR /model/app

# install dependencies
RUN pip install -r /model/requirements.txt 

# expose the port for API
EXPOSE 5000

# set environment variables
ENV ml_debug_level=1
ENV environment PRODUCTION

# run the api, replace later with Flask app running
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]