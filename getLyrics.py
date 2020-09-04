import os
import requests
import time

import trackList

API_KEY = os.environ["MUSIX_KEY"]

track_list = trackList.track_list
artist_query = trackList.artist_query

while not track_list :
    time.sleep(.25)

header = {
    "Accept": "text/plain"
}

lyrics = []
songCount = 0

for track in track_list :
    track_query = track.replace(" ", "%20")
    lyrics_request = f"https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_artist={artist_query}&q_track={track_query}&apikey={API_KEY}"
    try :
        res = requests.get(lyrics_request, headers=header)
    except :
        print(f"Failed to get Musixmatch lyrics on {track}")
        continue
    res_data = res.json()
    try :
        lyric = res_data["message"]["body"]["lyrics"]["lyrics_body"]
        lyrics.append(lyric)
        songCount += 1
    except :
        print(f"Failed to collect lyrics on {track}")
        continue

# print(f"{lyrics[0]}\n")
print(songCount)
