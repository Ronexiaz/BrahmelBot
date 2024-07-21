import GlobalLists
import random


def getWaiter():
    pickNum = random.randint(0, len(GlobalLists.PHOTOS) - 1)
    fileName = GlobalLists.PHOTOS[pickNum]
    return fileName


def getRandomID():
    pickID = random.randint(0, len(GlobalLists.IDS) - 1)
    return GlobalLists.IDS[pickID]

def getRandomPost():
    pickPost = random.randint(0, len(GlobalLists.SHITPOSTS) - 1)
    return GlobalLists.SHITPOSTS[pickPost]