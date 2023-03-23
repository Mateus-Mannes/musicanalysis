# Musicanalysis
musicanalysis is a Flask app that uses the Spotify API and the Spotipy python lib to create cool analysis about Music.
Master branch deployed at: https://musicanalysis.azurewebsites.net/

# Dependencies
The app is based in apotipy lib (https://spotipy.readthedocs.io/en/2.16.1/) and spotify web api (https://developer.spotify.com/)

# Usability
The app has 3 principal routes:

Home: index page, with a graphic map of the popularity of a genre

Profile: profile page, shows data about the user playlist, top genre, top artists and top tracks. In this page there is also an option to choose one playlist to analyze, that redirects to an other page with data about tracks and features

Search users profiles: search page, there you can search for another spotify user, by the user id or the share URL, and if the user exists and has public playlists, you will be redirected to a page with analysis about their tracks.


# Code
The struct of the project is like a MVC, with application.py as the controler, the classes from each route at models folder and the views at the templates folder. The images and some css classes are at the static folder and the JS code used is inside the views at the HTML files. In addition some auxiliary functions are divided into files in the project folder. The data from the index page map is been getting from https://github.com/Mateus-Mannes/top-country-tracks-api


# How to run
To o run the app first you need to install with PIP the requirements from requirements.txt file.

Then you need to setup the enviroments variables:

set SPOTIPY_CLIENT_ID=your-SPOTIPY_CLIENT_ID

set SPOTIPY_CLIENT_SECRET=your-SPOTIPY_CLIENT_SECRET

set SPOTIPY_REDIRECT_URI=http://127.0.0.1:5000/login (or other host)

set FLASK_APP=application.py

Take a look on how to register an app, get your CLIENT ID and SECRET and register a REDIRECT_URI here: https://developer.spotify.com/documentation/web-api/quick-start/

Then run the command "flask run" in the CMD.
