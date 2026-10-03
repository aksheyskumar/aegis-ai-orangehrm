pipeline {
    agent any
    environment {
        BASE_URL = 'https://opensource-demo.orangehrmlive.com'
        ENV = 'qa'
        BROWSER=chromium
        HEADLESS=false

    }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install .
                '''
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                sh '''
                    .venv/bin/python -m playwright install chromium
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    .venv/bin/python -m pytest tests/ui -v
                '''
            }
        }
    }
}