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
    var noteToDisplay = window.prompt("What is the index of the note you want?");
    if(localStorage.getItem(noteToDisplay) !== null) {
        result = localStorage.getItem(noteToDisplay);
    }
    if(result === null) {
        result = "No note saved";
    }
    document.getElementById('area').value = result;
}
function save() {
    if(check_web_storage_support() == true) {
        var area = document.getElementById("area");
        if(area.value != '') {
            localStorage.setItem(localStorage.length, area.value);
        }
        else {
            alert("Nothing to save");
        
        }

    }
}

function clear() {
    document.getElementById('area').value = "";
    localStorage.setItem(stor, area.value);
}