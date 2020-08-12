import os
from flask import Flask, session, request, redirect, render_template
from flask_session import Session
import spotipy
import uuid
from main import Look_For_User
from login import login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

caches_folder = './.spotify_caches/'
if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)


def session_cache_path():
    return caches_folder + str(session.get('uuid'))


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/logout', methods=['GET'])
def logout():
    os.remove(session_cache_path())
    session.clear()
    try:
        os.remove(session_cache_path())
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    return redirect('/')


@app.route('/login', methods=['GET'])
def login():
    if not session.get('uuid'):
        session['uuid'] = uuid.uuid4()
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-read-currently-playing playlist-modify-private',
                                                cache_path=session_cache_path(),
                                                show_dialog=True)
    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/profile')
    if not auth_manager.get_cached_token():
        # Step 2. Display sign in link when no token
        auth_url = auth_manager.get_authorize_url()
        return redirect(auth_url)


@app.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html')


@app.route('/create', methods=['GET'])
@login_required
def create_playlist():
    return render_template('create.html')


@app.route('/look users', methods=["GET", "POST"])
@login_required
def look_users():
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_path=session_cache_path())
    if request.method == 'POST':
        query = Look_For_User(request.form.get('username'), auth_manager)
        return render_template('look.html', name=query.name, cop=query.get_playlists(), img=query.img, genres=query.get_genres(), fav = query.get_artist()[0], genre = query.get_artist()[1], photo = query.get_artist()[2], incommon = query.get_incommon())
    if not auth_manager.get_cached_token():
        return redirect('/')
    return render_template('look.html', method='get')
