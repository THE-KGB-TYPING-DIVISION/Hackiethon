window.onload = function() {
        document.getElementById('area').value=localStorage.getItem(stor);
    
    }

function check_web_storage_support() {
    if(typeof(Storage) !== "undefined") {
        return(true);
    }
    else {
        alert("Web storage unsupported!");
        return(false);
    }
}
function display_saved_note() {
    if(localStorage.getItem(stor) !== null) {
        result = localStorage.getItem(stor);
    }
    if(result === null) {
        result = "No note saved";
    }
    document.getElementById('area').value = result;
}
display_saved_note();
function save() {
    
    var stor = 1;
    if(check_web_storage_support() == true) {
        var area = document.getElementById("area");
        if(area.value != '') {
            localStorage.setItem(stor + 1, area.value);
        }
        else {
            alert("Nothing to save");
        }

    }
    console.log(localStorage.length);
    for (var i = 0; i < localStorage.length; i++) {
        console.log(localStorage.getItem(localStorage.key(i)));
    }
}

function clear() {
    document.getElementById('area').value = "";
    localStorage.setItem(stor, area.value);
}