import random
import GlobalLists


class FRRoller:
    def __init__(self, rank, karma):
        self.rank = rank
        self.karma = karma

    def frLookup(self, roll, karma):
        rangeOf = GlobalLists.RANK_DICT[self.rank]
        total = roll + karma
        name = rangeOf[3]
        if total > rangeOf[2]:
            return 'RED', name
        elif total >= rangeOf[1]:
            return 'YELLOW', name
        elif total >= rangeOf[0]:
            return 'GREEN', name
        else:
            return 'WHITE', name

    def frRoll(self):
        roll = random.randint(1, 100)
        result, rankName = self.frLookup(roll, self.karma)
        message = ("rolled: " + str(roll) +
                   "\nRank: " + str(self.rank) + " (" + rankName + ")" +
                   "\nKarma added: " + str(self.karma) +
                   "\nTotal: " + str(roll + self.karma) +
                   "\nResult: **" + result + "**")
        return message
