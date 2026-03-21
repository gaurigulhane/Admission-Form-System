function validateForm() {

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let mobile = document.getElementById("mobile").value;
    let department = document.getElementById("department").value;
    let feedback = document.getElementById("feedback").value;
    let gender = document.querySelector('input[name="gender"]:checked');

    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    if (name == "") {
        alert("Name cannot be empty");
        return false;
    }

    if (!email.match(emailPattern)) {
        alert("Invalid Email");
        return false;
    }

    if (!/^\d{10}$/.test(mobile)) {
        alert("Invalid Mobile Number");
        return false;
    }

    if (!gender) {
        alert("Select Gender");
        return false;
    }

    if (department == "") {
        alert("Select Department");
        return false;
    }

    if (feedback.split(" ").length < 10) {
        alert("Minimum 10 words required");
        return false;
    }

    alert("Form Submitted Successfully!");
    return true;
}