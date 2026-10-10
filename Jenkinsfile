
pipeline {
    agent any

    stages {
        stage('Download Code / Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Show Python Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Python Program') {
            steps {
                sh 'python3 read.py'
            }
        }
    }
}
