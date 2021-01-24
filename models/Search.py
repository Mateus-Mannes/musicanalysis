import spotipy
from collections import Counter
import pandas as pd

class Search():

    def __init__(self, id, auth_manager):
        self.Spotify = spotipy.Spotify(auth_manager=auth_manager)
        self.Playlists = self.Spotify.user_playlists(id, limit=5)
        self.CurrentUserPlaylists = self.Spotify.current_user_playlists(limit=5)
        try:
            self.Name = self.Playlists["items"][0]["owner"]["display_name"]
        except:
            self.Name = id
        try:
            self.Image = self.Spotify.user(id)["images"][0]["url"]
        except:
            self.Image = "static/images/user.png"
        self.PlaylistsTracks = []
        for playlist in self.Playlists["items"]:
            self.PlaylistsTracks.append(self.Spotify.playlist_tracks(playlist["id"]))
        self.CurrentUserPlaylistsTracks = []
        for playlist in self.CurrentUserPlaylists["items"]:
            self.CurrentUserPlaylistsTracks.append(self.Spotify.playlist_tracks(playlist["id"]))

    def GetTopGenres(self):
        topGenres = []
        for playlistTracks in self.PlaylistsTracks:
            artistsCounter = 0
            artists = []
            for i in range(len(playlistTracks["items"])):
                if artistsCounter == 10:
                    break
                if playlistTracks["items"][i]["track"]["artists"][0]["id"] not in artists:
                    artists.append(playlist["items"][i]["track"]["artists"][0]["id"])
                    artistsCounter += 1
            artistFullData = self.Spotify.artists(artists)
            genres = []
            for i in range(len(artistFullData["artists"])):
                for genre in artistFullData["artists"][i]["genres"]:
                    genres.append(genre)
            counter = Counter(genres)
            mode = counter.most_common(1)[0][0]
            if mode not in topGenres:
                topGenres.append(mode)
        return topGenres

    def GetTopArtists(self):
        artists = []
        for playlistTracks in self.PlaylistsTracks:
            for track in playlistTracks["items"]:
                try:
                    artists.append(track["track"]["artists"][0]["id"])
                except:
                    break
        counter = Counter(artists)
        topArtist = counter.most_common(1)[0][0]
        artistData = self.Spotify.artist(topArtist)
        try:
            genre = artistData["genres"][0]
        except IndexError:
            genre = artistData["genres"]
        album = self.Spotify.artist_albums(topArtist)["items"][0]["id"]
        return {"artist": artistData, "genre": genre, "album": album}

    def get_incommon(self):
        usermusics = f.get_musics(self.playlistdata)
        mymusics = f.get_musics(self.myplaylistdata)
        return f.get_incommonmusics(usermusics, mymusics)