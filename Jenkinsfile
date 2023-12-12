pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh 'sh \'pip install -r requirements.txt\''
      }
    }

  }
  environment {
    DOCKER_COMPOSE_FILE = 'docker-compose.yml'
  }
}