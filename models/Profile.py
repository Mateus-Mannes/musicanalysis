import spotipy
from collections import Counter
import pandas as pd

class Profile():

    def __init__(self, auth_manager):
        self.Spotify = spotipy.Spotify(auth_manager=auth_manager)
        self.TopArtists = self.Spotify.current_user_top_artists()
        self.User = self.Spotify.me()
        try:
            self.Img = self.User["images"][0]["url"]
        except:
            self.Img = "templates/images/user.png"
        self.Playlists = self.Spotify.current_user_playlists()
        self.TopTracks = self.Spotify.current_user_top_tracks()

    def GetTopGenre(self):
        genres = []
        for i in range(len(self.TopArtists["items"])):
            for genre in self.TopArtists["items"][i]["genres"]:
                genres.append(genre)
        counter = Counter(genres)
        mode = counter.most_common(1)[0][0]
        return mode