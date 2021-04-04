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

function display_all() {
    
    var all_notes = ''
    
    for(var i =0; i < localStorage.length; i++) {
        if (localStorage.key(i) != 'highscore' && localStorage.key(i) != 'datetocount' && localStorage.key(i) != 'time') {
            all_notes = all_notes + localStorage.key(i) + ' ' + localStorage.getItem(localStorage.key(i)) + '\n';
        }
    }
    document.getElementById('all notes').value = all_notes;
}

function show_image(src, width, height, alt) {
    var img = document.createElement("img");
    img.src = src;
    img.width = width;
    img.height = height;
    img.alt = alt;
    
    // This next line will just add it to the <body> tag
    document.body.appendChild(img); 
  }
function big_save() {
    save();
    show_image('/static/images/MARK.jfif', 500, 500, 'marc');  
}