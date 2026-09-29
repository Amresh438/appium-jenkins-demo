// Works on both Windows and Linux/Mac Jenkins machines
def run(cmd) {
    if (isUnix()) { sh cmd } else { bat cmd }
}

pipeline {
    agent any

    stages {
        stage('Get Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    run('python -m pip install -r requirements.txt')
                }
            }
        }

        stage('Check Device') {
            steps {
                script {
                    // Shows connected phone/emulator. Should list at least one "device".
                    run('adb devices')
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    run('python -m pytest tests --junitxml=reports/results.xml --html=reports/report.html --self-contained-html')
                }
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/results.xml'
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
        }
        success { echo 'All tests passed!' }
        failure { echo 'Tests failed - check the report in Artifacts.' }
    }
}
