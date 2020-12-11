# musicanalysis
musicanalysis is a Flask app that uses the Spotify API and the Spotipy python lib to create cool analysis about Music.
Master branch deployed at: http://spmusicanalysis.herokuapp.com/

# dependencies
the app is based in apotipy lib (https://spotipy.readthedocs.io/en/2.16.1/) and spotify web api (https://developer.spotify.com/)

# usability
the app has 3 principal routes:

Home: index page, with a graphic map of the popularity of a genre

Profile: profile page, show data about the user playlist, top genre, top artists and top tracks. In this page there is also an option to choose one playlist to analyze, that redirect to an other page with data about tracks and features

Look users: search page, there you can search for an other spotify user, by the user id o the share url, and if this user exists and has public playlists, it will be redirected to an page with analysis about his tracks.


# code
Every route has an class, they are all at main.py file, and they are using some generic function to deal with api data, from the functions.py file. the data from the index page map is been getting from https://github.com/Mateus-Mannes/top-country-tracks-api


# how run
to run the app first you need to install with pip the requirements from requirements.txt file.

then you need to setup the enviroments variables:

set SPOTIPY_CLIENT_ID=your-SPOTIPY_CLIENT_ID

set SPOTIPY_CLIENT_SECRET=your-SPOTIPY_CLIENT_SECRET

set SPOTIPY_REDIRECT_URI=http://127.0.0.1:5000/login (or other host)

set FLASK_APP=application.py

take a look how register an app and get your CLIENT ID and SECRET and register a REDIRECT_URI here: https://developer.spotify.com/documentation/web-api/quick-start/

then run the command "flask run" in the cmd.


# deploy
the branch master of the repo is deployed at heroku (with automatic deploy when there is a push or commit), this is the reason of the Procfile. Take a look how to deploy an app like this in: https://www.youtube.com/watch?v=sqJSdJbOOU0
