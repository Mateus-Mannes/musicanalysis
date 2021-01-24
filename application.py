import os
from flask import Flask, session, request, redirect, render_template
from flask_session import Session
import spotipy
import uuid
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import requests, json
from models.Profile import Profile
from models.Playlist import Playlist
from models.Search import Search
from login_requirement import login_required
from erro_handler import apology
from check_user import check_user

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './flask_session/'
Session(app)

caches_folder = './spotify_caches/'
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)

def session_cache_path():
    return caches_folder + str(session.get('uuid'))

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

@app.route('/logout', methods=['GET'])
def logout():
    os.remove(session_cache_path())
    session.clear()
    return redirect('/')

@app.route('/login', methods=['GET'])
def login():
    if not session.get('uuid'):
        session['uuid'] = uuid.uuid4()
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-read-currently-playing playlist-modify-private user-read-recently-played user-top-read',
                                                cache_path=session_cache_path(),
                                                show_dialog=True)
    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/profile')
    if not auth_manager.get_cached_token():
        auth_url = auth_manager.get_authorize_url()
        return redirect(auth_url)

@app.route('/', methods=['GET'])
def index():
    # REQUEST TO GET TOP TRACKS DATA FROM API
    # SOURCE: https://github.com/Mateus-Mannes/top-country-tracks-api
    data = requests.get("http://mateusmedeiros.pythonanywhere.com/").json()
    genres = set({})
    for country in data:
        for track in data[country]:
            for genre in data[country][track]["Genres"]:
                genres.add(genre)
    return render_template('index/index.html', top_tracks_data=data, genres=genres)

@app.route('/profile', methods=['GET'])
@login_required
def profile():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path())
    profile = Profile(auth_manager)
    return render_template('profile/profile.html', profile=profile,genre=profile.GetTopGenre())
    
@app.route('/playlist-<id>', methods=["GET"])
@login_required
def playlist(id):
    playlist_id = id
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path())
    playlist = Playlist(playlist_id, auth_manager)
    return render_template('playlist/playlist.html', averages=playlist.GetAverages(), features=playlist.GetFeatures())

@app.route('/search', methods=["GET", "POST"])
@login_required
def search():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path())
    if request.method == 'POST':
        id = request.form.get('username')
        if "https://open.spotify.com/user/" in id:
            id = id.replace("https://open.spotify.com/user/", "")
        if "?si=" in id:
            temp = id.split("?si=")
            id = temp[0]
        if check_user(id, auth_manager):
            search = Search(id, auth_manager)

            if query.get_playlists() == []:
                return render_template('search/search.html', status="no playlists")

            return render_template('search/search.html', name=query.name,
                                                playlists=query.get_playlists(),
                                                img=query.img,
                                                genres=query.get_genres(),
                                                favoriteArtist = query.get_artist(),
                                                incommon = query.get_incommon())
        else:
            return render_template('search/search-form.html', status="notfound")
    return render_template('search/search-form.html', status="ok")

@app.route('/about', methods=["GET"])
def about():
    return render_template('about/about.html')
