pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/raufur-simanto/flask_app_with_docker', branch: 'main')
      }
    }

  }
  environment {
    DOCKER_COMPOSE_FILE = 'docker-compose.yml'
  }
}