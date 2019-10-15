function check_pwd_match() {
    var pwd_current = document.getElementById('pwd_input');
    var pwd_confirm = document.getElementById('pwd_confirm_input');
    if (pwd_current.value != pwd_confirm.value) {
        pwd_confirm.setCustomValidity("Passwords not match");
    } else {
        pwd_confirm.setCustomValidity("");
    }
};