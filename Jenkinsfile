pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/hassan-ahmed512/network-tools-api.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python.exe -m pip install flask pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest -v'
            }
        }
    }
}

