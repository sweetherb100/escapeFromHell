# https://labs.spotify.com/2014/02/28/how-to-shuffle-songs/

# import sys
# import codecs
# sys.stdin= codecs.getreader("utf-8")
# # (sys.stdin.detach())
# sys.stdout = codecs.getwriter("utf-8")
# (sys.stdout.detach())
from random import randint
import random


def shuffle(songs, artists):
    n = len(songs)
    info = []
    dict = {}

    # step1: let's construct vector of [(count of artists, artists)]
    for s in set(artists):
        info.append((artists.count(s), s))  # save as tuple

    # let's construct dict of [artists : [their songs]]
    for i in range(len(artists)):
        if artists[i] not in dict:
            dict[artists[i]] = [songs[i]]
        else:
            dict[artists[i]].append(songs[i])
            random.shuffle(dict[artists[i]])  # shuffle the songs of that artists to have different result every time

    info.sort(reverse=True)  # descending order

    # construct new data format
    infostr = []
    for i in range(len(info)):
        infostr.extend(dict[info[i][1]])

    # step 2: First distribute evenly the songs of most counted singers
    result = [None] * n

    # jump by 2 starting from index 0
    result[::2] = infostr[:(n + 1) // 2]

    # jump by 2 starting from 1 (the rest)
    result[1::2] = infostr[(n + 1) // 2:]  # using the rest of elements starting from (n+1)//2, distribute the rest

    return '\t'.join(map(str, result[::]))


# Enter your code here. Read input from STDIN. Print output to STDOUT
casecnt = int(input())
for i in range(casecnt):
    songs = [part for part in input().split("\t")]
    artists = [part for part in input().split("\t")]

    res = shuffle(songs, artists)
    print(res)

