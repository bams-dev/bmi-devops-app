pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-id')
        IMAGE_NAME = 'inzabamba/bmi-app'
    }

    stages {
        stage('Cloner le dépôt') {
            steps {
                git 'https://github.com/bams-dev/bmi-devops-app.git'
            }
        }

        stage('Tests') {
            steps {
                echo "Pas de test unitaire pour le moment"
            }
        }

        stage('Build Image Docker') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-id') {
                        docker.image("${IMAGE_NAME}").push('latest')
                    }
                }
            }
        }

        stage('Déploiement avec Docker Compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Notification') {
            steps {
                mail to: 'bambainza91@gmail.com',
                     subject: "Déploiement réussi",
                     body: "L'application BMI a été déployée avec succès !"
            }
        }
    }
}
