pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh '''// checkout branch
sudo checkout scm'''
      }
    }

  }
  environment {
    DOCKER_COMPOSE_FILE = 'docker-compose.yml'
  }
}