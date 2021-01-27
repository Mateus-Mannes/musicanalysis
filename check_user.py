import spotipy

def check_user(user, usuario):
    try:
        sp = spotipy.Spotify(auth_manager=usuario)
        playlists = sp.user_playlists(user, limit=5)
        return True
    except:
        return False
