import socket
import json
import xml.etree.ElementTree as xml

HOST = 'localhost'
PORT = 8000


def display(client, request):
    li = list(request.lower().split(" "))
    if "xml" in li:
        if "bollywood" in li:
            response = Bollywood_xml(li)
            client.send(response.encode())
        elif "hollywood" in li:
            response = Hollywood_xml(li)
            client.send(response.encode())
        else:
            print("Invalid Type")
    elif "json" in li:
        if "bollywood" in li:
            response = Bollywood_json(li)
            client.send(response.encode())
        elif "hollywood" in li:
            response = Hollywood_json(li)
            client.send(response.encode())
        else:
            print("Invalid Type")
    else:
        print("Invalid Type")


def Bollywood_xml(li):
    if "movies" in li and "songs" in li:
        tree = xml.parse("movie_songs_bollywood.xml")
        root = tree.getroot()
        response = []
        for movie_element in root.findall("movie"):
            movie_name = movie_element.text
            for song_element in movie_element.findall("song"):
                song_name = song_element.text
                response.append(song_name)
        return json.dumps(response)
    else:
        tree = xml.parse("movie_songs_bollywood.xml")
        root = tree.getroot()
        response = []
        for movie_element in root.findall("movie"):
            movie_name = movie_element.text
            response.append(movie_name)
        return json.dumps(response)
    

def Hollywood_xml(li):
    if "movies" in li and "songs" in li:
        tree = xml.parse("movie_songs_hollywood.xml")
        root = tree.getroot()
        response = []
        for movie_element in root.findall("movie"):
            movie_name = movie_element.text
            for song_element in movie_element.findall("song"):
                song_name = song_element.text
                response.append(song_name)
        return json.dumps(response)
    else:
        tree = xml.parse("movie_songs_hollywood.xml")
        root = tree.getroot()
        response = []
        for movie_element in root.findall("movie"):
            movie_name = movie_element.text
            response.append(movie_name)
        return json.dumps(response)
    

def Hollywood_json(li):
    if "movies" in li and "songs" in li:
        with open("movie_songs_hollywood.json", "r") as json_file:
            movie_songs = json.load(json_file)
        response = []
        for movie, songs in movie_songs.items():
            for song in songs:
                response.append(song)
        return json.dumps(response)
    else:
        with open("movie_songs_hollywood.json", "r") as json_file:
            movie_songs = json.load(json_file)
        response = list(movie_songs.keys())
        return json.dumps(response)
    

def Bollywood_json(li):
    if "movies" in li and "songs" in li:
        with open("movie_songs_bollywood.json", "r") as json_file:
            movie_songs = json.load(json_file)
        response = []
        for movie, songs in movie_songs.items():
            for song in songs:
                response.append(song)
        return json.dumps(response)
    else:
        with open("movie_songs_bollywood.json", "r") as json_file:
            movie_songs = json.load(json_file)
        response = list(movie_songs.keys())
        return json.dumps(response)
    

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    server.bind((HOST, PORT))
    print("Running the server on", HOST, PORT)
except Exception as e:
    print("Unable to bind the host and port:", e)


server.listen(1)


while True:
    client, address = server.accept()
    print("Successfully connected to Client", address[0], address[1])
    request = client.recv(1024).decode()
    print("Request by the client is:\n", request)
    display(client, request)
    client.close()
