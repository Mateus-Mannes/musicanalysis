import spotipy
import functions as f


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


class Profile():

    def __init__(self, usuario):
        self.auth = usuario
        self.sp = spotipy.Spotify(auth_manager=usuario)
        self.top = self.sp.current_user_top_artists()
        self.user = self.sp.me()
        self.img = f.get_image(self.user)
        self.name = f.get_current_name(self.user)

    def get_topartists(self):
        return f.get_topfive_artists(self.top)

    def get_playlists(self):
        playlistdata = self.sp.current_user_playlists()
        return f.get_playlistsnames(playlistdata)

    def get_topgenre(self):
        allgenres = f.get_allgenres(self.top)
        return f.get_mode(allgenres)

    def get_toptracks(self):
        toptracks = self.sp.current_user_top_tracks()
        return f.get_topfive_tracks(toptracks)

class Playlist_Statistics():

    def __init__(self, playlistid, usuario):
        self.sp = spotipy.Spotify(auth_manager=usuario)
        self.playlistdata = f.get_playlitsdata(playlistid, self.sp)
        self.audio_features = f.get_audiofeatures(self.playlistdata, self.sp)
        self.df = f.get_dataframe(self.playlistdata, self.audio_features)

    def get_mfeatures(self):
        mostpopular = f.maximum(self.df, "popularity")
        longest = f.maximum(self.df, "duration_ms")
        happiest = f.maximum(self.df, "valence")
        lesspopular = f.minimum(self.df, "popularity")
        shortest = f.minimum(self.df, "duration_ms")
        saddest = f.minimum(self.df, "valence")
        return mostpopular, longest, happiest, lesspopular, shortest, saddest

    def get_avgfeatures(self):
        danceability = round(self.df["danceability"].mean() * 100, 2)
        energy = round(self.df["energy"].mean() * 100, 2)
        acousticness = round(self.df["acousticness"].mean() * 100, 2)
        instrumentalness = round(self.df["instrumentalness"].mean() * 100, 2)
        valence = round(self.df["valence"].mean() * 100, 2)
        return danceability, energy, acousticness, instrumentalness, valence
