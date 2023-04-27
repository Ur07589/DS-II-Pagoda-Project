from Pagoda import PagodaClass
import csv
import string 
#from src.AVL Tree Implementation import AVLTree

class Track:
    def __init__(self, Artist: string, Url_spotify: string, Name: string, Album: string, Tempo: int, Url_Youtube: string, Youtubeviews: int, Likes: int, Spotifystreams: int):
        self.Artist=Artist
        self.Name=Name
        self.Album=Album
        self.Tempo=Tempo
        self.Url_Youtube=Url_Youtube
        self.Url_Spotify=Url_spotify
        self.Likes=Likes
        self.YoutubeViews=Youtubeviews
        self.Spotifyviews=Spotifystreams
        self.left=None 
        self.right=None

Trackarchive=[]

with open("./Spotify and Youtube.csv", 'r',encoding="utf8") as file:
    csvreader = csv.reader(file)
    c = 0
    for row in csvreader:
        if c == 0:
            continue
        obj = Track(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
        Trackarchive.append(obj)
        c+=1

PagodaTree=PagodaClass()
for i in Trackarchive:
    PagodaTree.insert(i)

min=PagodaTree.findextremes(1)
print(min)