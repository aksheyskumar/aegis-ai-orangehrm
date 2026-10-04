pipeline {
    agent any
    parameters {
        string(
            name: 'WORKERS',
            defaultValue: '2',
            description: 'Number of pytest-xdist workers'
        )
    }

    environment {
        BASE_URL = 'https://opensource-demo.orangehrmlive.com'
        ENV = 'qa'
        BROWSER = 'chromium'
        HEADLESS = 'true'
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
                    .venv/bin/python -m pytest tests/ui -v -n ${WORKERS} --alluredir=reports/allure-results
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    results: [[path: 'reports/allure-results']]
                ])
            }
        }
    }
}