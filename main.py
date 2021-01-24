import spotipy
import functions as f
from collections import Counter
import pandas as pd


class Search():

    def __init__(self, user, usuario):
        self.sp = spotipy.Spotify(auth_manager=usuario)
        self.playlists = self.sp.user_playlists(user, limit=5)
        self.myplaylists = self.sp.current_user_playlists(limit=5)
        self.name = f.get_name(self.playlists)
        if self.name == "no name":
            self.name = user
        self.img = f.get_image(self.sp.user(user))
        self.ids = f.get_ids(self.playlists)
        self.myids = f.get_ids(self.myplaylists)
        self.playlistdata = f.get_playlitsdata(self.ids, self.sp)
        self.myplaylistdata = f.get_playlitsdata(self.myids, self.sp)

    def get_playlists(self):
        return f.get_playlistsnames(self.playlists)

    def get_genres(self):
        genres = []
        for i in range(len(self.playlistdata)):
            playlist = self.playlistdata[i]
            artists = f.get_artistsids(playlist)
            artistFullData = self.sp.artists(artists)
            mode = (f.get_genres_mode(artistFullData))
            if mode not in genres:
                genres.append(mode)
        return genres

    def get_artist(self):
        allartists = f.get_allartists(self.playlistdata)
        artist = f.get_mode(allartists)
        artistdata = self.sp.artist(artist)
        artistname = artistdata["name"]
        genre = f.get_artistgenre(artistdata)
        photo = artistdata["images"][0]["url"]
        album = self.sp.artist_albums(artist)["items"][0]["id"]
        return {"name": artistname, "genre": genre, "photo": photo, "album": album}

    def get_incommon(self):
        usermusics = f.get_musics(self.playlistdata)
        mymusics = f.get_musics(self.myplaylistdata)
        return f.get_incommonmusics(usermusics, mymusics)