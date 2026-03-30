# Student Feedback Registration Form

## Project Structure
- `index.html`: The HTML form structure
- `style.css`: Visual styling using external CSS
- `script.js`: Client-side form validation rules
- `test_form.py`: Selenium automated test cases (pytest)
- `requirements.txt`: Python package dependencies for Selenium runs
- `Jenkinsfile`: Jenkins declarative pipeline configuration

## How to Run Locally

### View the Web Form
1. Simply double-click on `index.html` to open it in Chrome, Edge, or Firefox.
2. The form validates dynamically on submission.

### Run Selenium Automated Tests locally
1. Ensure you have Python installed locally and added to PATH. 
2. Open a terminal (PowerShell/CMD) in this directory: `C:\Users\Dell\.gemini\antigravity\scratch\StudentFeedbackForm`.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the tests:
   ```bash
   pytest test_form.py -v
   ```

## Jenkins Automation Setup Workflow

To automate test executing using Jenkins, follow these instructions:
1. **Install Jenkins**: Download and install Jenkins for Windows from [jenkins.io](https://www.jenkins.io/download/).
2. **Plugins Required**: Ensure the "Pipeline" and "JUnit" plugins are installed in the Jenkins dashboard.
3. **Create Job**:
   - Go to Jenkins Dashboard -> **New Item**.
   - Enter a name (e.g., `StudentFeedbackForm_Tests`) and select **Pipeline**, then click OK.
4. **Configure Pipeline**:
   - In the Configuration page under the **Pipeline** section, you can configure it via SCM (if you push this code to GitHub).
   - Alternatively, choose **Pipeline script** and copy-paste the contents of the `Jenkinsfile` directly into the script area.
   - Note: Since this Jenkinsfile assumes a local Windows build server context, it uses `bat` scripts to run Python commands.
5. **Run the Job**:
   - Save the configuration and click **Build Now**.
   - Check the **Console Output** of the build to see the `pip install` logs and test execution.
   - After the build finishes, view the generated **Test Result** trend directly on the Jenkins build page.
