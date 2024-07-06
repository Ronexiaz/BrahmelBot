import GlobalLists
import random


def getWaiter():
    pickNum = random.randint(0, len(GlobalLists.PHOTOS) - 1)
    fileName = GlobalLists.PHOTOS[pickNum]
    return fileName
