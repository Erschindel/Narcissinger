import os
import requests
import time


API_KEY = os.environ["MUSIX_KEY"]

class Lyrics () :
    def __init__ (self, tracks, a_query) :
        self.tracks = tracks
        self.a_query = a_query
        self.song_count = 0
        self.lyrics = []

    def get_lyrics (self) :
        # self.a_query = artist_info.get_track_list()

        # while self.tracks != tracks :
        # time.sleep(1)

        header = {
            "Accept": "text/plain"
        }

        lyrics = []
        song_count = 0

        for track in self.tracks :
            track_query = track.replace(" ", "%20")
            lyrics_request = f"https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_artist={self.a_query}&q_track={track_query}&apikey={API_KEY}"
            try :
                res = requests.get(lyrics_request, headers=header)
            except :
                print(f"Failed to get Musixmatch lyrics on {track}")
                continue
            res_data = res.json()
            try :
                lyric = res_data["message"]["body"]["lyrics"]["lyrics_body"]
                lyrics.append(lyric)
                song_count += 1
            except :
                print(f"Failed to collect lyrics on {track}")
                continue

        self.song_count = song_count
        self.lyrics = lyrics
