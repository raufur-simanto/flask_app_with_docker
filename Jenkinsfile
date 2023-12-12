pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh '''// Example checkout step
checkout([$class: \'GitSCM\', branches: [[name: \'main\']], userRemoteConfigs: [[url: \'https://github.com/raufur-simanto/flask_app_with_docker.git\']]])
'''
      }
    }

  }
  environment {
    DOCKER_COMPOSE_FILE = 'docker-compose.yml'
  }
}