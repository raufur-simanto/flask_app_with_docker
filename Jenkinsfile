pipeline {
  agent any
  stages {
    stage('dev') {
      steps {
        echo 'Hello'
      }
    }

  }
  environment {
    DOCKER_COMPOSE_FILE = 'docker-compose.yml'
  }
}