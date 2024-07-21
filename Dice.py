import random


class DiceRoller:
    def __init__(self, amt, type, modi):
        self.amt = amt
        self.type = type
        self.modi = modi

    def rollDice(self):
        totalRoll = 0
        allRolls = []
        for i in range(self.amt):
            newRoll = random.randint(1, self.type)
            allRolls.append(newRoll)
            totalRoll += newRoll

        rollOut = (" rolled: " + str(allRolls)
                   + "\nModifier given: " + str(self.modi)
                   + "\nTotal of rolled dice and modifier: "
                   + "**" + str(totalRoll + self.modi) + "**")

        return rollOut
