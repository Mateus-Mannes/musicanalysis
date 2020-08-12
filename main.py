import spotipy
from functions import get_name, get_image, get_genres_mode, get_ids, get_playlistsnames, get_artistsids, get_allartists, get_mode, get_musicnames, get_incommonmusics, get_artistgenre


class Look_For_User():

    def __init__(self, user, usuario):
        self.sp = spotipy.Spotify(auth_manager=usuario)
        self.playlists = self.sp.user_playlists(user, limit=5)
        self.myplaylists = self.sp.current_user_playlists(limit=5)
        self.name = get_name(self.playlists)
        self.img = get_image(self.sp.user(user))
        self.ids, self.myids = get_ids(self.playlists, self.myplaylists)
        self.playlistdata = []
        self.myplaylistdata = []
        for i in range(len(self.ids)):
            self.playlistdata.append(self.sp.user_playlist(user, self.ids[i]))
        for i in range(len(self.myids)):
            self.myplaylistdata.append(self.sp.user_playlist(self.sp.me()["id"], self.myids[i]))

    def get_playlists(self):
        return get_playlistsnames(self.playlists)

    def get_genres(self):
        genres = []
        for i in range(len(self.playlistdata)):
            playlist = self.playlistdata[i]
            artists = get_artistsids(playlist)
            artistFullData = self.sp.artists(artists)
            mode = (get_genres_mode(artistFullData))
            if mode not in genres:
                genres.append(mode)
        return genres

    def get_artist(self):
        allartists = get_allartists(self.playlistdata)
        artist = get_mode(allartists)
        artistdata = self.sp.search(q='artist:' + f"{artist}", type='artist')
        genre = get_artistgenre(artistdata)
        photo = artistdata["artists"]["items"][0]["images"][0]["url"]
        return artist, genre, photo

    def get_incommon(self):
        usermusics = get_musicnames(self.playlistdata)
        mymusics = get_musicnames(self.myplaylistdata)
        return get_incommonmusics(usermusics, mymusics)
