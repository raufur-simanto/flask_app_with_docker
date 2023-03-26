# Install Base Image
FROM python:3.10-slim-buster

# set working directory
WORKDIR /usr/app

# copy neccessary changing resources to img file system
COPY ./requirements.txt ./
# Install necessary dependencies
RUN pip install -r requirements.txt
COPY ./ ./

# Command for starting container
CMD ["flask", "run", "--host=0.0.0.0"]