pipeline {
    agent any

    environment {
        // Defines python path environments if needed
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                // In a real scenario, this would check out from Git:
                // git 'https://github.com/your-username/your-repo.git'
                // For a local directory, you might use the local plugin or run directly.
                echo 'Checking out code...'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                // Assuming Windows Jenkins agent with Python available in PATH
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Running pytest for Selenium automated tests...'
                // Create reports directory if it doesn't exist
                bat 'if not exist reports mkdir reports'
                // Run tests and generate JUnit XML report
                bat 'pytest test_form.py -v --junitxml=reports/result.xml'
            }
        }
    }

    post {
        always {
            // Archive the test reports
            junit 'reports/result.xml'
            echo 'Pipeline finished.'
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed. Please check the logs.'
        }
    }
}
