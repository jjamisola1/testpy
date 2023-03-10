#Deriving the latest base image
FROM python:latest

#Labels as key value pair
LABEL Maintainer="jamisojn"

# Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY test.py ./
#COPY server.py ./
COPY server2.py ./
COPY requirements.txt ./
COPY test1.py ./

RUN pip install -r requirements.txt
# Now the structure looks like this '/usr/app/src/test.py'

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

#CMD [ "python3", "./server.py"]
CMD [ "python3", "./server2.py"]
