
class Artists:

    def __init__(self, name, numberOfSongs, followers):
        self.name = name
        self.numberOfSogs = numberOfSongs
        self.songs = []
        self.followers = followers

    def addSong(self, song):
        self.songs.append(song)


