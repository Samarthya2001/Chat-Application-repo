import xml.etree.ElementTree as xml


def create_movie_songs_xml():
    movie_songs = {
        "Titanic": ["My Heart Will Go On", "Celine Dion", "Hymn to the Sea"],
        "The Lord of the Rings": ["May It Be", "Into the West", "Concerning Hobbits"],
        "Jurassic Park": ["Jurassic Park Theme", "Welcome to Jurassic Park", "T-Rex Rescue and Finale"],
        "Inception": ["Time", "Dream Is Collapsing", "No Time for Caution"],
        "The Dark Knight": ["The Dark Knight Theme", "Aggressive Expansion", "Why So Serious?"]
    }

    root = xml.Element("movies")
    for movie, songs in movie_songs.items():
        movie_element = xml.SubElement(root, "movie")
        movie_element.text = movie
        for song in songs:
            song_element = xml.SubElement(movie_element, "song")
            song_element.text = song
    tree = xml.ElementTree(root)

    tree.write("movie_songs_hollywood.xml", encoding="utf-8")


create_movie_songs_xml()