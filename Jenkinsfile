pipeline {
    agent any

    parameters {
        string(name: 'branch', defaultValue: 'main', description: 'Branch to build from')
    }

    stages {
        stage('Checkout and Run Tests') {
            steps {
                // Checkout the code from the repository
                checkout([$class: 'GitSCM', branches: [[name: "*/${params.branch}"]], userRemoteConfigs: [[url: 'https://github.com/RUSTEMATOR/Deposit-bible-test.git']]])

                // Install necessary dependencies
                sh 'pip3 install -r requirements.txt'  // Adjust if needed

                // Run the tests
                sh 'pytest -v /Users/rustemsamoilenko/Desktop/Playwright/Deposit_bible/test_deposit_bible.py'
            }
        }
    }

    post {
        success {
            echo 'Tests completed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
