
pipeline {
    agent any

    environment {
        PYTHON_VERSION = 'python3'
        USERNAME = credentials('ADMIN_USERNAME')
        PASSWORD = credentials('ADMIN_PASSWORD')
    }

    stages {
        stage('Download Code / Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Show Python Version') {
            steps {
                sh '$PYTHON_VERSION --version'
            }
        }

        stage('Run Python Program') {
            steps {
                sh '''
                    export username="$USERNAME"
                    export password="$PASSWORD"
                    "$PYTHON_VERSION" read.py
                '''
            }
        }
    }
}
