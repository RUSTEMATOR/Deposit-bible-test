pipeline {
    agent any

    parameters {
        string(name: 'branch', defaultValue: 'main', description: 'Branch to build from') // Changed 'master' to 'main
        string(name: 'url', defaultValue: 'https://www.kingbillycasino.com', description: 'URL to test')
        string(name: 'path', defaultValue: 'Desktop/Deposit bible screenshots', description: 'Path to test')
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

        stage('Test Run') {
            steps {
                script {
                    // Explicitly use the full path to bash
                    sh '''
                        /bin/bash -c "pip install pytest"
                        
                        # Build the command for running the tests
                        testCommand="pytest -s -k test_deposit_bible -m ${params.marker} --url ${params.url} --path ${params.path}"
                        
                        # Add the branch parameter if needed
                        if [ -n "${params.branch}" ]; then
                            testCommand+=" --branch ${params.branch}"
                        fi
                        
                        # Run the tests
                        $testCommand
                    '''
                }
            }
        }
    }
}
