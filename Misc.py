import GlobalLists
import random


def getWaiter():
    pickNum = random.randint(1, 2)
    fileName = ""
    if pickNum == 1:
        fileName = "more blood please.png"
    else:
        fileName = "more alchemical reagent please.png"

    return fileName
