pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        sh 'git branch: \'main\', url: \'https://github.com/raufur-simanto/flask_app_with_docker.git\''
      }
    }

  }
  environment {
    DOCKER_COMPOSE_FILE = 'docker-compose.yml'
  }
}