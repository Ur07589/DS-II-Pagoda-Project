from Pagoda import PagodaClass
from AVL_Tree_Implementation import AVLTree
import csv
import string 
import time
from memory_profiler import profile
#import matplotlib.pyplot as plt

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
        
        if c == 0 or row[7] == '':
            c+=1
            continue
        obj = Track(row[1],row[2],row[3],row[4],row[5],row[6],int(row[7]),row[8],row[9])
        c+=1
        Trackarchive.append(obj)

    # for line in file:
    #     data.append(line.strip().split(","))

# startA=time.time()
# avl_tree = AVLTree()
# root = None
# for row in data:
#     root = avl_tree.insert_node(root, row)
# endA=time.time()
# print(avl_tree.root)
# # Print the tree
# avl_tree.printHelper(root, "", True)

start=time.time()
PagodaTree=PagodaClass()
for i in Trackarchive:
    PagodaTree.insert(i)
end = time.time()

time_n=end-start
# time_l=endA-startA

print(PagodaTree.root.trackobj.Name)
print(PagodaTree.root.trackobj.Artist)

print(time_n)
# print(time_l)
