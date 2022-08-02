var count_genre = [['Country', 'Popularity']];
var genre = "pop";
for (contry in top_tracks_data)
{
    if (contry === "Global"){ continue; }
    var count = 0;
    var tracks = top_tracks_data[contry];
    for (track in tracks) {
        genres = top_tracks_data[contry][track]["Genres"]
        for(var h = 0; h < genres.length; h++)
        {
            if(genres[h] === genre)
            {
                count = count + 1;
            }
        }
    }
count_genre.push([contry, count]);
}
  
document.getElementById('input').onkeyup = function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("input");
    filter = input.value.toUpperCase();
    div = document.getElementById("dropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      txtValue = a[i].textContent || a[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
}

function changeCountry(genre) {
    var count_genre = [['Country', 'Popularity']];
    for (contry in top_tracks_data) {
        if (contry === "Global") { continue; }
        var count = 0;
        var tracks = top_tracks_data[contry];
        for (track in tracks) {
            genres = top_tracks_data[contry][track]["Genres"]
            for (var h = 0; h < genres.length; h++) {
                if (genres[h] === genre) {
                    count = count + 1;
                }
            }
        }
        count_genre.push([contry, count]);
    }
    google.charts.load('current', {
        'packages': ['geochart'],
        'mapsApiKey': 'AIzaSyATtbryoSOyktqnHutX5ek3N93bvcP2Q70'
    });
    google.charts.setOnLoadCallback(drawRegionsMap);

    function drawRegionsMap() {
        var data = google.visualization.arrayToDataTable(count_genre);

        var options = {};

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);
    }
    document.getElementById("dropdown").classList.toggle("show");
    var button = document.getElementById("dropbtn");
    button.innerHTML = genre;
    var mapTitle = document.getElementById("mapTitle");
    mapTitle.innerHTML = "<b>current popularity of " + genre + " in the world</b>";
}

$(window).resize(function() { 
    location.reload();
});

