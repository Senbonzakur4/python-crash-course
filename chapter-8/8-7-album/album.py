# 8.7 Album

def make_album(artist_name, album_title, number_of_songs = None):
    """Return a dictionary containing information about an album."""
    album = {
            "Artist": artist_name,
            "Album": album_title,
            "Songs": number_of_songs,
    }
    return album

album = make_album("Gorillaz", "Demon Days")
print(album)
album = make_album("Hatsune Miku", "Re:Dial", 10)
print(album)
album = make_album("Mago de Oz", "Gaia II: La Voz Dormida", 12)
print(album)