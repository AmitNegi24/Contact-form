function select_change() {
    var z = document.getElementById("form_action").selectedIndex;
    var z1 = document.getElementsByTagName("option")[z].value;
    alert("Form action changed to " + z1);
    }
    function myfunction() {
    if (local()) {
    // Calling Validation function.
    //select option value from select tag and storing it in a variable.
    var x = document.getElementById("form_action").selectedIndex;
    var action = document.getElementsByTagName("option")[x].value;
    if (action !== "") {
    document.getElementById("form_id").action = action;
    document.getElementById("form_id").submit();
    } else {
    alert("Please set form action");
    }
    }
    }
    const local = e=> {
        let formData={
            fname:document.getElementById('fname').value,
            lname:document.getElementById('lname').value,
            email:document.getElementById('email').value,
            pwd:document.getElementById('pwd').value
        }
        localStorage.setItem('formData',JSON.stringify(formData));
        console.log(localStorage.getItem('formData'));
        e.preventDefault();
    }