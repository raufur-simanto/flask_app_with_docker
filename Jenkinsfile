// pipeline{
//     agent{
//         label 'experiment'
//     }
    
//     triggers{
//          pollSCM('* * * * *') // Polls SCM every minute
//     }
    
//     stages{
//         stage('Checkout'){
//             steps{
//                 git(url: 'https://github.com/raufur-simanto/flask_app_with_docker', branch: 'main')
//             }
//         }
//         stage('Logs'){
//             steps{
//                 // show files and directories
//                 sh 'ls -l'
//             }
            
//         }
//         stage('Build Image'){
//             steps{
//                 sh 'docker build -t raufurrahman/flask_app_with_docker:v.0.1 --network host .'
//             }
//         }
        
//         stage('Push Image to docker hub'){
//             steps {
//                 withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
//                     sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
//                     sh 'docker push raufurrahman/flask_app_with_docker:v.0.1'
//                 }
//             }
//         }
        
//         stage('Check and Stop Container') {
//              steps {
//                  script {
//                      def containerName = 'flask_app'
                    
//                      // Check if the container exists
//                      def containerExists = sh(script: "docker ps -a --format '{{.Names}}' | grep '^${containerName}\$'", returnStatus: true)
                    
//                      if (containerExists == 0) {
//                          echo "Container '${containerName}' found. Stopping it..."
                        
//                          // Stop the container
//                          sh "docker stop ${containerName}"
                        
//                          // Remove the container
//                          sh "docker rm ${containerName}"
//                      } else {
//                          echo "Container '${containerName}' not found."
//                      }
//                  }
//              }
//          }
//         stage('Deploy'){
//             steps{
//                 // Use lock to prevent concurrent deployment
//                     sh 'docker-compose up -d --build'
//             }
          
//         }
//     }
   
// }

pipeline {
  agent any 
  
  environment{
      DOCKER_TAG = getDockerTag()
  }
  
  stages {
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
                sh 'docker build -t raufurrahman/flask_app_with_docker:${DOCKER_TAG} --network host .'
            }
        }
        stage('Push Image to docker hub'){
            steps {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                        sh 'docker push raufurrahman/flask_app_with_docker:${DOCKER_TAG}'
                    }
                }
        }
        
            
        stage('Deploy to k8s cluster ') {
          steps {
              
              sh 'chmod u+x changeTag.sh'
              sh './changeTag.sh ${DOCKER_TAG}'
              
              withKubeCredentials(kubectlCredentials: [[caCertificate: '', clusterName: 'cluster', contextName: '', credentialsId: 'SECRET_TOKEN', namespace: 'default', serverUrl: 'https://10.7.0.11:6443']]) {
                      sh 'curl -LO "https://storage.googleapis.com/kubernetes-release/release/v1.20.5/bin/linux/amd64/kubectl"'  
                      sh 'chmod u+x ./kubectl'  
                      sh './kubectl apply -f site-visit.yaml'
                      sh './kubectl get pods -n default'
                  
              }
                
            }
            
        }
        
    }
  
}
  
//   def getDockerTag(){
//       def tag = sh script: 'git rev-parse HEAD', returnStdout: true
//       return tag
//   }
  
  def getDockerTag() {
    def gitCommitHash = sh(script: 'git rev-parse HEAD', returnStdout: true).trim()
    def githubBranchName = env.BRANCH_NAME
    return "main-${gitCommitHash}"
}

  
