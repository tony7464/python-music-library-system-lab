class Song:
    """A single track in the music library.

    Instance attributes describe one song. Class attributes accumulate
    library-wide stats so we can report totals, unique lists, and counts
    without storing every Song elsewhere.
    """

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Every new song immediately updates library-wide stats.
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total number of songs created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Record a genre once so `genres` stays a unique list."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Record an artist once so `artists` stays a unique list."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Tally songs per genre; start the key at 1 if it is new."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Tally songs per artist; start the key at 1 if it is new."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

        # Keep the spec name (`artists_count`) aligned with the test name.
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1
