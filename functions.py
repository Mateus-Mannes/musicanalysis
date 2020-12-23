import spotipy
from collections import Counter
import pandas as pd

def check_user(user, usuario):
    try:
        sp = spotipy.Spotify(auth_manager=usuario)
        playlists = sp.user_playlists(user, limit=5)
        return True
    except:
        return False

def get_current_name(user):
    if user['display_name'] != '':
        return user['display_name']
    else:
        return user['id']
    

def get_name(playlists):
    try:
        name = playlists["items"][0]["owner"]["display_name"]
    except:
        name = "no name"
    return name


def get_image(userdata):
    try:
        img = userdata["images"][0]["url"]
    except:
        img = "static/imgs/user.png"
    return img


def get_ids(playlists):
    ids = []
    for i in range(len(playlists["items"])):
        ids.append(playlists["items"][i]["id"])
    return ids


def get_playlitsdata(ids, sp):
    playlistdata = []
    if type(ids) == list:
        for i in range(len(ids)):
            playlistdata.append(sp.playlist_tracks(ids[i]))
    else:
        playlistdata = sp.playlist_tracks(ids)
    return playlistdata


def get_playlistsnames(playlists):
    if playlists["items"] != []:
        playlistsnames = []
        for i in range(len(playlists["items"])):
            nameSize = len(playlists["items"][i]["name"])
            if nameSize > 23:
                playlistsnames.append((playlists["items"][i]["name"][0:20] + "...", (playlists["items"][i]["id"])))
            else:
                playlistsnames.append((playlists["items"][i]["name"], (playlists["items"][i]["id"])))
    else:
        return playlists["items"]
    return playlistsnames


def get_mode(x):
    counter = Counter(x)
    mode = counter.most_common(1)[0][0]
    return mode


def get_artistsids(playlist):
    artists_counter = 0
    artists = []
    for i in range(len(playlist["items"])):
        if artists_counter == 10:
            break
        if playlist["items"][i]["track"]["artists"][0]["id"] not in artists:
            artists.append(playlist["items"][i]["track"]["artists"][0]["id"])
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
        for i in range(len(playlist["items"])):
            try:
                artists.append(playlist["items"][i]["track"]["artists"][0]["id"])
            except:
                break
    return artists


def get_musics(playlistdata):
    musics = []
    for i in range(len(playlistdata)):
        playlist = playlistdata[i]
        for i in range(len(playlist["items"])):
            try:
                musics.append(playlist["items"][i]["track"]["id"])
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


def get_topfive_artists(top):
    topfive = []
    for i in range(5):
        topfive.append([top["items"][i]["name"], top["items"][i]["id"], top["items"][i]["images"][0]["url"]])
    return(topfive)


def get_topfive_tracks(top):
    topfive = []
    for i in range(5):
        topfive.append([top["items"][i]["name"], top["items"][i]["id"]])
    return(topfive)


def get_allgenres(artists):
    genres = []
    for i in range(len(artists["items"])):
        for genre in artists["items"][i]["genres"]:
            genres.append(genre)
    return genres


def get_audiofeatures(playlistdata, sp):
    ids = []
    features = []
    ids = get_tracks_ids(playlistdata)
    for x in ids:
        features.append(sp.audio_features(x))
    return features

def get_tracks_ids(tracks):
    ids = []
    for i in range(len(tracks["items"])):
        try:
            ids.append(tracks["items"][i]["track"]["id"])
        except:
            continue
    return ids

def get_dataframe(playlistdata, audio_features):
    ids = []
    ids = get_tracks_ids(playlistdata)
    df = pd.DataFrame(columns=["name", "popularity", "danceability", "energy", "acousticness", "instrumentalness", "valence", "duration_ms"], index = ids)
    for i in range(len(playlistdata["items"])):
        try:
            df.loc[playlistdata["items"][i]["track"]["id"], "name"] = playlistdata["items"][i]["track"]["name"]
            df.loc[playlistdata["items"][i]["track"]["id"], "popularity"] = playlistdata["items"][i]["track"]["popularity"]
        except:
            continue
    for audio in audio_features:
        df.loc[audio[0]["id"], "danceability"] = audio[0]["danceability"]
        df.loc[audio[0]["id"], "energy"] = audio[0]["energy"]
        df.loc[audio[0]["id"], "danceability"] = audio[0]["danceability"]
        df.loc[audio[0]["id"], "acousticness"] = audio[0]["acousticness"]
        df.loc[audio[0]["id"], "instrumentalness"] = audio[0]["instrumentalness"]
        df.loc[audio[0]["id"], "valence"] = audio[0]["valence"]
        df.loc[audio[0]["id"], "duration_ms"] = audio[0]["duration_ms"]
    return df


def maximum(df, column):
    maximum = [(df['name'][df[column] == df[column].max()].values[0]),
               (df.index[df[column] == df[column].max()].tolist()[0])]
    return maximum


def minimum(df, column):
    minimum = [(df['name'][df[column] == df[column].min()].values[0]),
               (df.index[df[column] == df[column].min()].tolist()[0])]
    return minimum
