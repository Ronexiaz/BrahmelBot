import random
import fantasynames as names
import GlobalLists


class RetainerGen:
    retList = []

    def __init__(self, levMax, levMin, amt):
        self.levMax = levMax
        self.levMin = levMin
        self.amt = amt

    def genCLN(self):
        randLevel = random.randint(self.levMin, self.levMax)
        if randLevel == 0:
            randClass = "Human"
        else:
            randClass = GlobalLists.CLASS_LIST[random.randint(0, GlobalLists.CLASS_LIST_LENGTH - 1)]

        randNum = random.randint(1, 3)

        if randClass == "Elf":
            randName = names.elf()
        elif randClass == "Dwarf":
            randName = names.dwarf()
        elif randClass == "Gnome" or randClass == "Halfling":
            randName = names.hobbit()
        elif randNum == 1:
            randName = names.anglo()
        elif randNum == 2:
            randName = names.french()
        else:
            randName = names.human()

        randCLN = "**" + str(randName) + "**, level " + str(randLevel) + ": " + randClass

        return randCLN

    def genAttr(self):
        randAttr1 = GlobalLists.ATTR_LIST[random.randint(1, 292)]
        randAttr2 = GlobalLists.ATTR_LIST[random.randint(1, 292)]
        randAttr3 = GlobalLists.ATTR_LIST[random.randint(1, 292)]

        if randAttr2 == randAttr1: randAttr2 = GlobalLists.ATTR_LIST[random.randint(1, 292)]
        if randAttr3 == randAttr2: randAttr3 = GlobalLists.ATTR_LIST[random.randint(1, 292)]

        randAttrs = " (" + randAttr1 + ", " + randAttr2 + ", " + randAttr3 + ") "

        return randAttrs

    def genAlignment(self):
        randAlNum = random.randint(1, 1001)

        if randAlNum <= 17: randAlignment = " [Chaotic Evil]"
        elif randAlNum <= 56: randAlignment = " [Neutral Evil]"
        elif randAlNum <= 106: randAlignment = " [Lawful Evil]"
        elif randAlNum <= 176: randAlignment = " [Chaotic Good]"
        elif randAlNum <= 253: randAlignment = " [Lawful Neutral]"
        elif randAlNum <= 348: randAlignment = " [Chaotic Neutral]"
        elif randAlNum <= 512: randAlignment = " [True Neutral]"
        elif randAlNum <= 751: randAlignment = " [Neutral Good]"
        else: randAlignment = " [Lawful Good]"

        return randAlignment

    def genRet(self):
        currCLN = self.genCLN()
        currAttrs = self.genAttr()
        currAln = self.genAlignment()

        currRet = currCLN + currAln + currAttrs
        return currRet

    def genList(self):
        self.retList = []
        for i in range(self.amt):
            newRet = self.genRet()
            self.retList.append(newRet)
        return self.retList

    def printList(self):
        if self.levMax < self.levMin:
            return GlobalLists.LVL_ERROR

        self.genList()

        msg = ""

        for i in self.retList:
            msg += ("- " + i + "\n")

        return msg
