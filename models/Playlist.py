import spotipy
from collections import Counter
import pandas as pd

class Playlist():

    def __init__(self, playlistId, auth_manager):
        self.Spotify = spotipy.Spotify(auth_manager=auth_manager)
        self.PlaylistData = self.Spotify.playlist_tracks(playlistId)
        tracksIds = []
        for i in range(len(tracks["items"])):
            try:
                tracksIds.append(tracks["items"][i]["track"]["id"])
            except:
                continue
        AudioFeatures = []
        for id in tracksIds:
            AudioFeatures.append(self.Spotify.audio_features(id))
        self.DataFrame = pd.DataFrame(columns=["name", "popularity", "danceability", "energy", "acousticness", "instrumentalness", "valence", "valence"], index = tracksIds)
        for i in range(len(self.PlaylistData["items"])):
            try:
                self.DataFrame.loc[self.PlaylistData["items"][i]["track"]["id"], "name"] = self.PlaylistData["items"][i]["track"]["name"]
                self.DataFrame.loc[self.PlaylistData["items"][i]["track"]["id"], "popularity"] = self.PlaylistData["items"][i]["track"]["popularity"]
            except:
                continue
        for feature in AudioFeatures:
            self.DataFrame.loc[feature[0]["id"], "danceability"] = audio[0]["danceability"]
            self.DataFrame.loc[feature[0]["id"], "energy"] = audio[0]["energy"]
            self.DataFrame.loc[feature[0]["id"], "danceability"] = audio[0]["danceability"]
            self.DataFrame.loc[feature[0]["id"], "acousticness"] = audio[0]["acousticness"]
            self.DataFrame.loc[feature[0]["id"], "instrumentalness"] = audio[0]["instrumentalness"]
            self.DataFrame.loc[feature[0]["id"], "valence"] = audio[0]["valence"]
            self.DataFrame.loc[feature[0]["id"], "valence"] = audio[0]["valence"]
              
    def GetFeatures(self):
        features = {}
        features["mostpopular"] = self.DataFrame.index[self.DataFrame[popularity] == self.DataFrame[popularity].max()].tolist()[0]
        features["longest"] = self.DataFrame.index[self.DataFrame[duration_ms] == self.DataFrame[duration_ms].max()].tolist()[0]
        features["happiest"] = self.DataFrame.index[self.DataFrame[valence] == self.DataFrame[valence].max()].tolist()[0]
        features["lesspopular"] = self.DataFrame.index[self.DataFrame[popularity] == self.DataFrame[popularity].min()].tolist()[0]
        features["shortest"] = self.DataFrame.index[self.DataFrame[duration_ms] == self.DataFrame[duration_ms].min()].tolist()[0]
        features["saddest"] = self.DataFrame.index[self.DataFrame[valence] == self.DataFrame[valence].min()].tolist()[0]
        return features

    def GetAverages(self):
        averages = {}
        averages["danceability"] = round(self.DataFrame["danceability"].mean() * 100, 2)
        averages["energy"] = round(self.DataFrame["energy"].mean() * 100, 2)
        averages["acousticness"] = round(self.DataFrame["acousticness"].mean() * 100, 2)
        averages["instrumentalness"] = round(self.DataFrame["instrumentalness"].mean() * 100, 2)
        averages["valence"] = round(self.DataFrame["valence"].mean() * 100, 2)
        return averages