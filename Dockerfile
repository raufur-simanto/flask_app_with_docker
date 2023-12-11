# Install Base Image
# FROM python:3.10-slim-buster

# # set working directory
# WORKDIR /usr/app

# # copy neccessary changing resources to img file system
# COPY ./requirements.txt ./
# # Install necessary dependencies
# RUN pip install -r requirements.txt
# COPY ./ ./

# # Command for starting container
# CMD ["flask", "run", "--host=0.0.0.0"]

# Assuming you are using Python as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Specify the command to run your application
CMD ["python", "app.py"]
