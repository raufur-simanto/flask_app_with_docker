pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh '''
sh \'git checkout main\''''
      }
    }

  }
  environment {
    DOCKER_COMPOSE_FILE = 'docker-compose.yml'
  }
}