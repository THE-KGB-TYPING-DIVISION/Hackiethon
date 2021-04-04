window.onload = function() {
    /*document.getElementById('menulink').onclick = function() {
        var menu = document.getElementById('menu');
        if(menu.className != 'shownmenu') {
            menu.className = 'shownmenu';
        }
        else {
            menu.className = 'hiddenmenu';
        }*/
        var stor = 'stuff';
        document.getElementById('area').value=localStorage.getItem(stor)
    }
var stor = 'stuff';
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
    var stor = 'stuff';
    if(check_web_storage_support() == true) {
        var area = document.getElementById("area");
        if(area.value != '') {
            localStorage.setItem(stor, area.value);
        }
        else {
            alert("Nothing to save");
        }
    }
}
function clear() {
    var stor = 'stuff';
    document.getElementById('area').value = "";
    localStorage.setItem(stor, area.value);
}