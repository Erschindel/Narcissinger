from trackList import Tracks
from getLyrics import Lyrics


keywords = ["I", "my", "me", "mine", "myself"]
musix_warning = "...  ******* This Lyrics is NOT for Commercial use ******* "

class Artist () :

    def __init__ (self, user_input) :
        self.user_input = user_input
        self.artist_info = []
        self.final_tracks = []

    def setup (self) :
        artist_info = Tracks(self.user_input)
        artist_info.get_track_list()
        self.artist_info = artist_info

        final_tracks = Lyrics(artist_info.track_list, artist_info.artist_query)
        final_tracks.get_lyrics()
        self.final_tracks = final_tracks

    def main (self) :
        self.setup()

        track_list = self.artist_info.track_list
        artist_query = self.artist_info.artist_query
        initial_lyrics = self.final_tracks.lyrics
        songCount = self.final_tracks.song_count

        lyrics_str = " ".join(initial_lyrics)
        lyrics_warning = lyrics_str.replace("\n", " ")
        lyrics = lyrics_warning.replace(musix_warning, " ")

        selfish_words = 0

        for selfish in keywords :
            for lyric in lyrics.split(" ") :
                if lyric == selfish :
                    selfish_words += 1

        # print(f"selfish words total: {selfish_words}")
        lyrics_length = len(lyrics.split(" "))
        print(f"Percentage of selfish words per song: {100 * selfish_words / lyrics_length}%")

print(f"First enter A = Artist(ARTIST_NAME), then do A.main()")
