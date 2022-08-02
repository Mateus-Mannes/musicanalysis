var dropdownItens = document.querySelectorAll('.dropdown-item')
for(let i = 0; i < dropdownItens.length; i++){
    dropdownItens[i].onclick = function () {
        document.getElementById("dropdownMenuButton").hidden = true;
        document.getElementById("dropdown-spinner").hidden = false;
    };
}