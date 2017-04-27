
class Artist:

    def __init__(self, name, tracks, followers):
        self.name = name
        self.tracks = tracks
        self.songs = []
        self.followers = followers

    def addSong(self, song):
        self.songs.append(song)


