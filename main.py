import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import Counter


def userdata(user):
    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    return sp.current_user_saved_tracks()


class Playlists():

    def __init__(self, user, usuario):
        self.sp = spotipy.Spotify(auth_manager=usuario)
        self.playlists = self.sp.user_playlists(user, limit=5)
        self.myplaylists = self.sp.user_playlists(self.sp.me()["id"], limit=5)
        try:
            self.nome = self.playlists["items"][0]["owner"]["display_name"]
        except:
            self.nome = "this user"
        try:
            self.img = self.sp.user(user)["images"][0]["url"]
        except:
            self.img = "no"
        self.ids = []
        for i in range(len(self.playlists["items"])):
            self.ids.append(self.playlists["items"][i]["id"])
        self.myids = []
        for i in range(len(self.myplaylists["items"])):
            self.myids.append(self.myplaylists["items"][i]["id"])
        self.music_playlists = []
        for i in range(len(self.ids)):
            self.music_playlists.append(self.sp.user_playlist(user, self.ids[i]))
        self.my_musics = []
        for i in range(len(self.myids)):
            self.my_musics.append(self.sp.user_playlist(self.sp.me()["id"], self.myids[i]))

    def pegar_playlists(self):
        if self.playlists["items"] != []:
            x = []
            for i in range(len(self.playlists["items"])):
                x.append(self.playlists["items"][i]["name"])
            return x, self.img
        else:
            return "no", self.img

    def pegar_generos(self):
        pgenres = []
        for i in range(len(self.music_playlists)):
            artists_counter = 0
            artists = []
            playlist = self.music_playlists[i]
            for i in range(len(playlist["tracks"]["items"])):
                if artists_counter == 10:
                    break
                if playlist["tracks"]["items"][i]["track"]["artists"][0]["id"] not in artists:
                    artists.append(playlist["tracks"]["items"][i]["track"]["artists"][0]["id"])
                    artists_counter += 1
            artistFullData = self.sp.artists(artists)
            generos = []
            for i in range(len(artistFullData["artists"])):
                for genero in artistFullData["artists"][i]['genres']:
                    generos.append(genero)
            moda = Counter(generos)
            if moda.most_common(1)[0][0] not in pgenres:
                pgenres.append(moda.most_common(1)[0][0])
        return pgenres

    def pegar_artista(self):
        artists = []
        for i in range(len(self.music_playlists)):
            playlist = self.music_playlists[i]
            for i in range(len(playlist["tracks"]["items"])):
                artists.append(playlist["tracks"]["items"][i]["track"]["artists"][0]["name"])
        moda = Counter(artists)
        fav = moda.most_common(1)[0][0]
        # print(f"O artista mais frequente de {self.nome} é {fav}! \n")
        artist = self.sp.search(q='artist:' + f"{fav}", type='artist')
        genre = str(artist["artists"]["items"][0]["genres"][0])
        genre = genre.replace("'", "")
        genre = genre.replace("[", "")
        genre = genre.replace("]", "")
        # print(f"Gênero: {genre}\n")
        foto = artist["artists"]["items"][0]["images"][0]["url"]
        # print(foto)
        artistData = [fav, genre, foto]
        return artistData

    def pegar_comuns(self):
        musics = []
        mymusics = []
        comuns = []
        for i in range(len(self.music_playlists)):
            playlist = self.music_playlists[i]
            for i in range(len(playlist["tracks"]["items"])):
                musics.append([playlist["tracks"]["items"][i]["track"]["name"], playlist["tracks"]["items"][i]["track"]["artists"][0]["name"]])

        for i in range(len(self.my_musics)):
            my_playlist = self.my_musics[i]
            for i in range(len(my_playlist["tracks"]["items"])):
                mymusics.append([my_playlist["tracks"]["items"][i]["track"]["name"], my_playlist["tracks"]["items"][i]["track"]["artists"][0]["name"]])
        for m in musics:
            if m in mymusics:
                comuns.append(m)
        try:
            return comuns[0:5]
        except:
            return comuns
            #  print(f"Algumas músicas que você tem em comum com {self.nome} são: \n")
            # try:
            # for c in comuns[0:5]:
            # print(c[0] + " - " + c[1])
            # except:
            # for c in comuns:
            # print(c[0] + " - " + c[1])

# analyze =  Playlists("12170240389")
# analyze.pegar_playlists()
# analyze.pegar_generos()
# analyze.pegar_artista()
# analyze.pegar_comuns()
