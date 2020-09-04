import sys
import requests
import time

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import spotifyAuth


artist = input("Enter artist name: ")
artist_query = artist.replace(" ", "%20")

request = "https://api.spotify.com/v1/search?q=%s&type=artist" % artist_query

token = spotifyAuth.access_token
header = {
    "Authorization" : f"Bearer {token}"
}

try :
    r = requests.get(request, headers = header)
except :
    print("Failed to connect to Spotify")

response_data = r.json()
artist_id = response_data["artists"]["items"][0]["id"]

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

response = sp.artist_top_tracks(artist_id)

track_list = [track['name'] for track in response['tracks']]

# print(track_list)
