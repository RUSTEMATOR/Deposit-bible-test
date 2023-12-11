pipeline {
    agent any

    parameters {
        string(name: 'branch', defaultValue: 'main', description: 'Branch to build from')
        string(name: 'url', defaultValue: 'https://www.kingbillycasino.com', description: 'URL to test')
        string(name: 'path', defaultValue: '/Users/rustemsamoilenko/Desktop/Playwright/Deposit_bible/test_deposit_bible.py', description: 'Path to test')
        string(name: 'marker', defaultValue: '', description: 'Parameters for pytest mark')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('SCM') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: "*/${params.branch}"]], userRemoteConfigs: [[url: 'https://github.com/RUSTEMATOR/Deposit-bible-test.git']]])
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies, including playwright
                    sh '/usr/local/bin/python3 -m pip install -r requirements.txt'
                    sh '/usr/local/bin/python3 -m pip install playwright'
                }
            }
        }

        stage('Test Run') {
            steps {
                script {
                    // Explicitly use the full path to bash
                    def command = """
                       sudo -E /bin/bash -c \'
                            /usr/local/bin/python3 -m pip install pytest &&
                            /usr/local/bin/python3 -m pytest -s -k test_deposit_bible -m \${params.marker} --url \${params.url} --path \${params.path} &&
                            echo "Tests completed successfully"\'
                    """
                    sh returnStatus: true, script: command
                }

