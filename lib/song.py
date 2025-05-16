class Song:
    count = 0
    artists = []
    genres = []
    
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)


    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else: 
            cls.genre_count.update({genre: 1})

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else: 
            cls.artist_count[artist] = 1


# # Test
# pop = Song('Saints', 'Jay-z', 'hipop')
# pop = Song('Hollow', 'Ricky', 'hipop')
# pop = Song('Lowzm', 'Nmbye', 'Jazz')
# print(pop.genre)

# print(pop.count)
# print(pop.genres)
# # print(pop.artists)

# # add to genre count function call
# # Song.add_to_genre_count()
# print(Song.genre_count)