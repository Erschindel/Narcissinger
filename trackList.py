import sys
import requests
import time

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import spotifyAuth


class Tracks () :
    def __init__(self, artist_name) :
        self.artist_name = artist_name
        self.artist_query = artist_name.replace(" ", "%20")
        self.track_list = []

    def send_auth (self) :
        request = "https://api.spotify.com/v1/search?q=%s&type=artist" % self.artist_query

        token = spotifyAuth.access_token
        header = {
            "Authorization" : f"Bearer {token}"
        }
        try :
            r = requests.get(request, headers = header)
        except :
            print("Failed to connect to Spotify")

        response_data = r.json()
        return(response_data)

    def get_track_list (self) :
        top_tracks = self.send_auth()
        artist_id = top_tracks["artists"]["items"][0]["id"]
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        response = sp.artist_top_tracks(artist_id)

        track_list = [track['name'] for track in response['tracks']]

        self.track_list = track_list
