// Get the query parameters from the URL
const urlParams = new URLSearchParams(window.location.search);

// Check if the 'error' query parameter exists
if (urlParams.has('invalidCredentials')) {
    // Create an error banner
    const errorBanner = document.createElement('div');
    errorBanner.textContent = 'Invalid credentials. Please try again.';
    errorBanner.style.backgroundColor = 'red';
    errorBanner.style.color = 'white';
    errorBanner.style.padding = '10px';
    errorBanner.style.marginBottom = '10px';

    // Insert the error banner at the top of the body
    document.body.insertBefore(errorBanner, document.body.firstChild);
}

if (urlParams.has('updatedHash')) {
    // Create an error banner
    const errorBanner = document.createElement('div');
    errorBanner.textContent = 'Next login, the hash will be updated.';
    errorBanner.style.backgroundColor = 'green';
    errorBanner.style.color = 'white';
    errorBanner.style.padding = '10px';
    errorBanner.style.marginBottom = '10px';

    // Insert the error banner at the top of the body
    document.body.insertBefore(errorBanner, document.body.firstChild);
}

function validatePassword() {
    var newPassword = document.getElementsByName('newpassword')[0];
    var confirmPassword = document.getElementsByName('confirmpassword')[0];

    if (newPassword.value !== confirmPassword.value) {
        alert("Passwords do not match.");
        return false;
    } else {
        return true;
    }
}