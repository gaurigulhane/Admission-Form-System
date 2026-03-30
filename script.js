function validateForm() {
    let isValid = true;

    // Reset all error messages
    clearErrors();
    document.getElementById('successMessage').style.display = 'none';

    // Validate Student Name
    const name = document.getElementById('studentName').value.trim();
    if (name === '') {
        showError('nameError', 'Student Name should not be empty');
        isValid = false;
    }

    // Validate Email
    const email = document.getElementById('email').value.trim();
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email === '') {
        showError('emailError', 'Email should not be empty');
        isValid = false;
    } else if (!emailPattern.test(email)) {
        showError('emailError', 'Email should be in proper format');
        isValid = false;
    }

    // Validate Mobile Number
    const mobile = document.getElementById('mobile').value.trim();
    const mobilePattern = /^[0-9]+$/; 
    if (mobile === '') {
        showError('mobileError', 'Mobile Number should not be empty');
        isValid = false;
    } else if (!mobilePattern.test(mobile)) {
        showError('mobileError', 'Mobile Number should contain valid digits only');
        isValid = false;
    }

    // Validate Department
    const department = document.getElementById('department').value;
    if (department === '') {
        showError('deptError', 'Department should be selected');
        isValid = false;
    }

    // Validate Gender
    const genders = document.getElementsByName('gender');
    let genderSelected = false;
    for (let i = 0; i < genders.length; i++) {
        if (genders[i].checked) {
            genderSelected = true;
            break;
        }
    }
    if (!genderSelected) {
        showError('genderError', 'At least one gender option should be selected');
        isValid = false;
    }

    // Validate Feedback Comments
    const feedback = document.getElementById('feedback').value.trim();
    if (feedback === '') {
        showError('feedbackError', 'Feedback Comments should not be blank');
        isValid = false;
    } else {
        const wordCount = feedback.split(/\s+/).filter(word => word.length > 0).length;
        if (wordCount < 10) {
            showError('feedbackError', 'Feedback Comments should meet minimum length of 10 words');
            isValid = false;
        }
    }

    if (isValid) {
        document.getElementById('successMessage').style.display = 'block';
        return false; // Prevent traditional submission to show success message and easily test via Selenium
    }

    return false; // Prevent traditional submission if invalid
}

function showError(elementId, message) {
    document.getElementById(elementId).innerText = message;
}

function clearErrors() {
    const errorElements = document.getElementsByClassName('error-message');
    for (let i = 0; i < errorElements.length; i++) {
        errorElements[i].innerText = '';
    }
    document.getElementById('successMessage').style.display = 'none';
}
