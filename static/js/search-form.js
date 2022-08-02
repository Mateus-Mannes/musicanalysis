document.getElementById('search-button').onclick = function () {
    if (document.querySelector("input").value != "") {
        document.getElementById("search-button").hidden = true;
        document.getElementById("search-spinner").hidden = false;
    }
};

document.getElementById('exampleModal').addEventListener('hidden.bs.modal', event => {
    notFoundLabel = document.querySelector('#notFoundLabel');
    if(notFoundLabel != null){
        document.querySelector('#notFoundLabel').hidden = true;
    }  
    noPlaylistLabel = document.querySelector('#noPlaylistLabel');
    if(noPlaylistLabel != null){
        document.querySelector('#noPlaylistLabel').hidden = true;
    } 
    document.querySelector('#getUrlLabel').hidden = false;
    document.querySelector('#getUrlImg').hidden = false;
});