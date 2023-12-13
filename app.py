from flask import Flask
import redis
import logging

app = Flask(__name__)

# configure logger
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.DEBUG)


redis_host = 'redis-server'
redis_port = 6379

redis_client = redis.Redis(host=redis_host, port=redis_port)
visits = 0
redis_client.set('visits', 0)


@app.route('/')
def home():
    val = int(redis_client.get('visits'))
    app.logger.info(val)
    redis_client.set('visits', int(val) + 1)

    return f"My Total visits: {val}"


if __name__ == '__main__':
    app.run()

# pipeline {
#     agent {
#         label 'experiment'
#     }
    
#     environment {
#         DOCKER_COMPOSE_VERSION = '1.29.2'
#         DOCKER_COMPOSE_FILE = 'docker-compose.yml'
#         DOCKER_COMPOSE_PROJECT_NAME = 'Check-Visits'
#     }

#     stages {
#         stage('Connection'){
#             steps{
#                 script {
#                     echo "Connected successfully!!"
#                 }
#             }
#         }
        
#         stage('Checkout') {
#             steps {
#                 script {
#                     // Checkout the code from GitHub
#                     git branch: 'main', url: 'https://github.com/raufur-simanto/flask_app_with_docker.git'
#                 }
#             }
#         }

#         stage('Build and Deploy with Docker Compose') {
#             steps {
#                 script {

#                     // Set Docker Compose project name
#                     sh "export COMPOSE_PROJECT_NAME=${DOCKER_COMPOSE_PROJECT_NAME}"

#                     // Build and deploy using Docker Compose
#                     sh "docker-compose -f ${DOCKER_COMPOSE_FILE} up --build"
#                 }
#             }
#         }
#     }

#     post {
#         always {
#             // Clean up, if needed
#             script {
#                 // Stop and remove containers
#                 sh "docker-compose -f ${DOCKER_COMPOSE_FILE} down"
#             }
#         }
#     }
# }
