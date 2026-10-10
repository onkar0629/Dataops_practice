
pipeline {
    agent any

    environment {
        PYTHON_VERSION = 'python3'
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
                sh '$PYTHON_VERSION read.py'
            }
        }
    }
}
