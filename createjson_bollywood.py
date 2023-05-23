import json

def create_movie_songs_json():

    movie_songs = {
        "Kabhi Khushi Kabhie Gham": ["Kabhi Khushi Kabhie Gham", "Bole Chudiyan", "Suraj Hua Madham"],
        "Dilwale Dulhania Le Jayenge": ["Tujhe Dekha Toh", "Mehndi Laga Ke Rakhna", "Ruk Ja O Dil Deewane"],
        "Kuch Kuch Hota Hai": ["Kuch Kuch Hota Hai", "Tujhe Yaad Na Meri Aayee", "Ladki Badi Anjani Hai"],
        "Gully Boy": ["Apna Time Aayega", "Mere Gully Mein", "Doori"],
        "Padmaavat": ["Ghoomar", "Khalibali", "Binte Dil"]
    }

    with open("movie_songs_bollywood.json", "w") as json_file:
        json.dump(movie_songs, json_file, indent=4)


create_movie_songs_json()