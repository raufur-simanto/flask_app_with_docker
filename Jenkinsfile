pipeline{
    agent{
        label 'experiment'
    }
    
    triggers{
         pollSCM('* * * * *') // Polls SCM every minute
    }
    
    stages{
        stage('Checkout'){
            steps{
                git(url: 'https://github.com/raufur-simanto/flask_app_with_docker', branch: 'main')
            }
        }
        stage('Logs'){
            steps{
                // show files and directories
                sh 'ls -l'
            }
            
        }
        stage('Build Image'){
            steps{
                sh 'docker build -t raufurrahman/flask_app_with_docker:v.0.1 --network host .'
            }
        }
        
        stage('Push Image to docker hub'){
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    sh 'docker push raufurrahman/flask_app_with_docker:v.0.1'
                }
            }
        }
        
        stage('Check and Stop Container') {
             steps {
                 script {
                     def containerName = 'flask_app'
                    
                     // Check if the container exists
                     def containerExists = sh(script: "docker ps -a --format '{{.Names}}' | grep '^${containerName}\$'", returnStatus: true)
                    
                     if (containerExists == 0) {
                         echo "Container '${containerName}' found. Stopping it..."
                        
                         // Stop the container
                         sh "docker stop ${containerName}"
                        
                         // Remove the container
                         sh "docker rm ${containerName}"
                     } else {
                         echo "Container '${containerName}' not found."
                     }
                 }
             }
         }
        stage('Deploy'){
            steps{
                // Use lock to prevent concurrent deployment
                    sh 'docker-compose up -d --build'
            }
          
        }
    }
   
}