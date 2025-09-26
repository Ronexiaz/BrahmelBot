class Jukebox:
    tracks = ['music\\Fabula Ultima (Main Theme).mp3']

    def __init__(self, musicOption):
        self.musicOption = musicOption

    def setMusic(self, newMusic):
        self.musicOption = newMusic

    def play(self):
        pass