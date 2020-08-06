from flask import Flask, flash, jsonify, redirect, render_template, request, session
import startup
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from collections import Counter
from main import Playlists

from spotipy.oauth2 import SpotifyClientCredentials
app = Flask(__name__)
app.secret_key = '2092189'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    #response = startup.getUser()
    return redirect('/callback/')
 
@app.route('/callback/')
def call():
    analyze = Playlists('marianamannes')
    y = analyze.pegar_comuns()
    return render_template('index.html', X=y)



