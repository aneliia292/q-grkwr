import random


class MusicAlbum:


    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist


def play_random_track(self):


    random_track = random.choice (self.tracklist)
print ("Playing random track:", random_track)

# Пример использования класса MusicAlbum
album = MusicAlbum ("The Dark Side of the Moon", "Pink Floyd", 1973, "Progressive Rock",
                    ["Speak to Me", "Breathe", "On the Run", "Time", "The Great Gig in the Sky", "Money", "Us and Them",
                     "Any Colour You Like", "Brain Damage", "Eclipse"])

print ("Album title:", album.title)
print ("Artist:", album.artist)
print ("Release year:", album.release_year)
print ("Genre:", album.genre)

album.play_random_track ()
