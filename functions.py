from collections import Counter
import spotipy


def check_user(user, usuario):
    sp = spotipy.Spotify(auth_manager=usuario)
    try:
        sp.user(user)
        return True
    except:
        return False


def get_name(playlists):
    try:
        name = playlists["items"][0]["owner"]["display_name"]
    except:
        name = "this user"
    return name


def get_image(userdata):
    try:
        img = userdata["images"][0]["url"]
    except:
        img = "no"
    return img


def get_ids(playlists, myplaylists):
    ids = []
    myids = []
    for i in range(len(playlists["items"])):
        ids.append(playlists["items"][i]["id"])
    for i in range(len(myplaylists["items"])):
        myids.append(myplaylists["items"][i]["id"])
    return ids, myids


def get_playlistsnames(playlists):
    if playlists["items"] != []:
        playlistsnames = []
        for i in range(len(playlists["items"])):
            playlistsnames.append((playlists["items"][i]["name"], (playlists["items"][i]["id"])))
    else:
        playlistsnames = "no"
    return playlistsnames


def get_mode(x):
    counter = Counter(x)
    mode = counter.most_common(1)[0][0]
    return mode


def get_artistsids(playlist):
    artists_counter = 0
    artists = []
    for i in range(len(playlist["tracks"]["items"])):
        if artists_counter == 10:
            break
        if playlist["tracks"]["items"][i]["track"]["artists"][0]["id"] not in artists:
            artists.append(playlist["tracks"]["items"][i]["track"]["artists"][0]["id"])
            artists_counter += 1
    return artists


def get_genres_mode(artistFullData):
    genres = []
    for i in range(len(artistFullData["artists"])):
        for genre in artistFullData["artists"][i]["genres"]:
            genres.append(genre)
    mode = get_mode(genres)
    return mode


def get_allartists(playlistdata):
    artists = []
    for i in range(len(playlistdata)):
        playlist = playlistdata[i]
        for i in range(len(playlist["tracks"]["items"])):
            try:
                artists.append(playlist["tracks"]["items"][i]["track"]["artists"][0]["id"])
            except:
                break
    return artists


def get_musics(playlistdata):
    musics = []
    for i in range(len(playlistdata)):
        playlist = playlistdata[i]
        for i in range(len(playlist["tracks"]["items"])):
            try:
                musics.append(playlist["tracks"]["items"][i]["track"]["id"])
            except:
                break
    return musics


def get_incommonmusics(usermusics, mymusics):
    incommon = []
    for m in usermusics:
        if m in mymusics:
            incommon.append(m)
    try:
        return incommon[0:5]
    except:
        return incommon


def get_artistgenre(artistdata):
    try:
        genre = artistdata["genres"][0]
    except IndexError:
        genre = artistdata["genres"]
    return genre
