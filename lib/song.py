class Song:
    
    count = 0
    genres = list()
    artists = list()
    genre_count = dict()
    artist_count = dict()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.append(self.genre)
        Song.artists.append(self.artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)


    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.apppend(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # iterate over the genres list and populate a dictionary with the key/value pairs
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # iterate over the artists list and populate a dictionary with the key/value pairs
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1  
        else:
            cls.artist_count[artist] = 1  