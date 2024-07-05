import random

class Stats:
    statList = []

    def __init__(self):
        pass

    def genStat(self):
        currStat = []
        statSum = 0

        for x in range(3):
            currRoll = random.randint(1, 6)
            currStat.append(currRoll)
            statSum += currRoll

        currStat.append(statSum)

        return currStat

    def printStats(self):
        allStats = ""

        for i in range(6):
            self.statList.append(self.genStat())

        for j in self.statList:
            allStats += "- [" + str(j[0]) + ", " + str(j[1]) + ", " + str(j[2]) + "] = **" + str(j[3]) + "**\n"

        return allStats