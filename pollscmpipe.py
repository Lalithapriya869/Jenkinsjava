pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking for changes...'
            }
        }

        stage('Run Python File') {
            steps {
                bat '"C:\\Users\\LalithaPriya\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" Jenkinsfile1.py'
            }
        }
    }

    post {
        success {
            echo 'Build Triggered by Poll SCM ✅'
        }
    }
}
