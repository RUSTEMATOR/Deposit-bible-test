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
                checkout([$class: 'GitSCM', branches: [[name: "*/${params.branch}"]], userRemoteConfigs: [[url: 'https://github.com/RUSTEMATOR/Deposit-bible-test.git']]])
            }
        }


    stage('Test Run') {
        steps {
            script {
                echo "URL: ${params.url}"
                echo "Path: ${params.path}"
                echo "Marker: ${params.marker}"
                sh "/usr/local/bin/python3 -m pytest -s -k test_deposit_bible -m ${params.marker} --url ${params.url} --path ${params.path}"
            }
        }
    }
}

