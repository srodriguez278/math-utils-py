pipeline {
    agent any

    environment {
        PYTHON = "C:\\Python313\\python.exe"
    }

    stages {
        stage('Install and Test') {
            steps {
                bat '''
                "%PYTHON%" -m venv .venv
                .venv\\Scripts\\python -m pip install --upgrade pip
                .venv\\Scripts\\pip install -r requirements.txt
                .venv\\Scripts\\pytest --junitxml=pytest-report.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'pytest-report.xml'
        }
    }
}
