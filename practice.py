from song import Song
def print_songs(song_list):
    for song in song_list:
        print(song)
songs = [
    Song("tv off", "Kendrick Lamar", 3.7),
    Song("Alright", "Kendrick Lamar", 3.5)
]

print_songs(songs)