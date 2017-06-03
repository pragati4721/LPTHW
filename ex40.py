class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def smas(self):
        for line in self.lyrics:
            print line
hbd = Song(["Happy birthday to you","I don't want to get sued","So I'll stop right there"])
bop = Song(["They rally around the family","with pockets full of shells"])
hbd.smas()
bop.smas()
