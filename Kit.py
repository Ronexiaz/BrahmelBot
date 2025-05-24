import random


class FullKit:
    def __init__(self, classoption, level):
        self.classoption = classoption
        self.level = level

    def assembleKit(self):
        selfCombatKit = combatKit(self.classoption)
        selfOtherKit = otherKit(self.classoption, self.level)

        combatKitString = "**PERSON**:\n"
        for equip in selfCombatKit:
            combatKitString += equip + "\n"

        otherKitString = "**BACKPACK**:\n"
        for equip in selfOtherKit:
            otherKitString += equip + "\n"

        fullKitString = combatKitString + "\n" + otherKitString
        return fullKitString


def combatKit(classoption):
    kitList = []
    match classoption:
        case 'CLERIC':
            kitList.append(chooseRandomFromList(['Club', 'Mace', 'Sling', 'Staff', 'War Hammer']))
            if random.randint(1, 2) == 2: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))

    return kitList


def otherKit(classoption, level):
    kitList = []
    match classoption:
        case 'CLERIC':
            kitList.append('Torches [' + str(random.randint(1, 12)) + ']')
            if random.randint(1, 4) < 4: kitList.append('Holy Water [' + str(random.randint(1, 4)) + ']')
            if random.randint(1, 2) == 2: kitList.append('Rope [' + str(random.randint(1, 4) * 50) + '\']')
            if random.randint(1, 2) == 2: kitList.append('Pole (10\', Wooden)')
            if random.randint(1, 10) > 7: kitList.append('Potion of Healing')
            kitList.append('Holy Symbol')
            kitList.append('Rations (Iron, 7 days)')
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
    return kitList


def chooseRandomFromList(givenList):
    randPick = random.randint(0, len(givenList) - 1)
    return givenList[randPick]


def goldCalc(level):
    goldCt = random.randint(1, (level % 5) + 6) * (2 + (level % 5))
    return goldCt
