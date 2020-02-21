Node{ stages(){
  stage(“checkout”){
      git branch: 'e2e', url: 'https://github.com/yahelron/World-of-Games_P3.git'
    }
    stage(“Run playbook”){
    dir ('C:\\code\github.com\\projects\\World of Games3\\World-of-Games_P3\\tests')
    bat 'e2e_guest.py'
    }
  }
}
