pipeline {
    agent any

    stages {
        stage('Compile') {
            steps {
                bat 'javac javajenkins1.java'
            }
        }

        stage('Run') {
            steps {
                bat 'java javajenkins1'
            }
        }
    }
}
