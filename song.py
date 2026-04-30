class Song:
    def _init_(self, name , artist, length):
        self.name = name
        self.artist = artist
        self.length = length
    my_song = Song("tv off", "Kendrick Lamar", 3.7)
    print(my_song.get_length_in_seconds())