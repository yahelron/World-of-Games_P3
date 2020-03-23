node {
    stage ('checkout') {
      git branch: 'e2e', url: 'https://github.com/yahelron/World-of-Games_P3.git'
    }
    stage("Env Variables") {

                echo "The build number is ${env.BUILD_NUMBER}"
                echo "You can also use \${BUILD_NUMBER} -> ${BUILD_NUMBER}"
                echo "this is your worksp ${WORKSPACE}"
            }
    stage("Deploy") {
        dir ("C:\\terraform\\devops-test"){
        bat 'terraform apply -auto-approve'
        sleep(70)
        bat 'terraform output public_ip >current_public_ip.txt'
      }
    }
    stage("Check e2e guess game")	{
        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE'){
        dir ("${WORKSPACE}\\tests"){
          def serverip = readFile(file: 'C:\\terraform\\devops-test\\current_public_ip.txt')
          echo "this is your worksp ${serverip}"
          bat "python e2e_guest.py --ip=${serverip}"}}
    }
    stage("Check e2e memory game")	{
        dir ("${WORKSPACE}\\tests"){
          def serverip = readFile(file: 'C:\\terraform\\devops-test\\current_public_ip.txt')
          bat "python e2e_memory.py --ip=${serverip}"
          }
    }
<<<<<<< HEAD

=======
    stage("Delete Server") {
        dir ("C:\\terraform\\devops-test"){
        bat 'terraform destroy -auto-approve'
      }
    }
>>>>>>> e2e
}