# 8.8 User Albums

def make_album(artist_name, album_title, number_of_songs = None):
    """Return a dictionary containing information about an album."""
    album = {
            "Artist": artist_name,
            "Album": album_title,
            "Songs": number_of_songs,
    }
    return album

while True:
    print("\nWelcome to the Album Maker!\n\nEnter 'q' at any time to quit.")
    artist_name = input("\nEnter the artist name: ")
    
    if artist_name == 'q':
        break

    album_title = input("\nEnter the album title: ")
    
    if album_title == 'q':
        break

    number_of_songs = input("\nEnter the number of songs in the album (optional):\n"
          "Press Enter to skip. ")
    
    if number_of_songs == 'q':
        break
    elif number_of_songs == '':
        number_of_songs = None
    else:
        number_of_songs = int(number_of_songs)

    album = make_album(artist_name, album_title, number_of_songs)

    print("\nYour album has been created:")

    for key, name in album.items():
        if name is not None:
            print(f"{key}: {name}")

    print("\n")