import json
def create_movie_songs_json():

    movie_songs = {
        "Titanic": ["My Heart Will Go On", "Celine Dion", "Hymn to the Sea"],
        "The Lord of the Rings": ["May It Be", "Into the West", "Concerning Hobbits"],
        "Jurassic Park": ["Jurassic Park Theme", "Welcome to Jurassic Park", "T-Rex Rescue and Finale"],
        "Inception": ["Time", "Dream Is Collapsing", "No Time for Caution"],
        "The Dark Knight": ["The Dark Knight Theme", "Aggressive Expansion", "Why So Serious?"]
    }

    with open("movie_songs_hollywood.json", "w") as json_file:
        json.dump(movie_songs, json_file, indent=4)

create_movie_songs_json()