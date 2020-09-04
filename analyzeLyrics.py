import getLyrics
import trackList

track_list = trackList.track_list
artist_query = trackList.artist_query
initial_lyrics = getLyrics.lyrics
songCount = getLyrics.songCount

keywords = ["I", "my", "me", "mine", "myself"]
musix_warning = "...  ******* This Lyrics is NOT for Commercial use ******* "

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
