pipeline {
agent { label 'aws' }
environment {
      // will use to help to skip a stage if in case of value change
      Var1 = "0"
  }
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/yahelron/World-of-Games.git'
            }
        }
        stage('build') {
            steps {
                 sh 'sudo docker-compose build'
            }
        }
        stage('run parallel') {
          failFast true
          parallel {
            stage('run docker-compose') {
              steps {
                sh 'sudo docker-compose up &'
              }
            }
            stage('test') {
              agent { label 'master' }
              when {
                // stage won't be skipped as long as Var1 == 0, build number is even
                environment name: "Var1", value: "0"
              }      
              steps {
                dir ('C:\\code\\github.com\\projects\\World of Games\\tests') {
                  sleep time: 30, unit: 'SECONDS'
                  bat '''
                  python e2e.py
                  @IF NOT %ERRORLEVEL% == 0 EXIT /b %ERRORLEVEL%
                  '''
                }
              }
            }
          }
        }
        stage('Finalize') {
           agent { label 'aws' }
          steps {
              echo 'delete env'
              sh 'sudo docker-compose -f  /jenkins/workspace/Devops_Proj/docker-compose.yml down'
              sh 'sudo docker rmi -f devopsproj_flasc_server python'
              echo 'Done'
          
          }
        }
    }
}
