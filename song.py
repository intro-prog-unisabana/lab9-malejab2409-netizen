class Song:
    def _init_(self, name , artist, length):
        self.name = name
        self.artist = artist
        self.length = length
    def get_length_in_seconds(self):
        return self.length * 60
   