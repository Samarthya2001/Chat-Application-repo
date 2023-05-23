import xml.etree.ElementTree as xml

def create_movie_songs_xml():
    movie_songs = {
        "Kabhi Khushi Kabhie Gham": ["Kabhi Khushi Kabhie Gham", "Bole Chudiyan", "Suraj Hua Madham"],
        "Dilwale Dulhania Le Jayenge": ["Tujhe Dekha Toh", "Mehndi Laga Ke Rakhna", "Ruk Ja O Dil Deewane"],
        "Kuch Kuch Hota Hai": ["Kuch Kuch Hota Hai", "Tujhe Yaad Na Meri Aayee", "Ladki Badi Anjani Hai"],
        "Gully Boy": ["Apna Time Aayega", "Mere Gully Mein", "Doori"],
        "Padmaavat": ["Ghoomar", "Khalibali", "Binte Dil"]
    }
    root = xml.Element("movies")
    for movie, songs in movie_songs.items():
        movie_element = xml.SubElement(root, "movie")
        movie_element.text = movie
        for song in songs:
            song_element = xml.SubElement(movie_element, "song")
            song_element.text = song

    tree = xml.ElementTree(root)
    tree.write("movie_songs_bollywood.xml", encoding="utf-8")


create_movie_songs_xml()