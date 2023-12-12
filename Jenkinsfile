pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh '''// checkout branch
checkout scm'''
      }
    }

  }
  environment {
    DOCKER_COMPOSE_FILE = 'docker-compose.yml'
  }
}