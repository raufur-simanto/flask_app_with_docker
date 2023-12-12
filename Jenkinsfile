pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh '''
sudo \'git checkout main\''''
      }
    }

  }
  environment {
    DOCKER_COMPOSE_FILE = 'docker-compose.yml'
  }
}