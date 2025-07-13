import random
import GlobalLists
from fictional_names import name_generator


def genAlignment(classOption):
    randAlNum = random.randint(1, 1001)

    match classOption:
        case "Assassin":
            if randAlNum <= 17:
                randAlignment = " [Chaotic Evil]"
            elif randAlNum <= 56:
                randAlignment = " [Neutral Evil]"
            elif randAlNum <= 176:
                randAlignment = " [Chaotic Good]"
            elif randAlNum <= 348:
                randAlignment = " [Chaotic Neutral]"
            elif randAlNum <= 512:
                randAlignment = " [Neutral Good]"
            else:
                randAlignment = " [True Neutral]"
        case "Druid":
            if randAlNum <= 17:
                randAlignment = " [Neutral Evil]"
            elif randAlNum <= 253:
                randAlignment = " [Lawful Neutral]"
            elif randAlNum <= 348:
                randAlignment = " [Chaotic Neutral]"
            elif randAlNum <= 512:
                randAlignment = " [True Neutral]"
            else:
                randAlignment = " [Neutral Good]"
        case "Paladin":
            if randAlNum <= 56:
                randAlignment = " [Lawful Evil]"
            elif randAlNum <= 253:
                randAlignment = " [Lawful Neutral]"
            else:
                randAlignment = " [Lawful Good]"

        case "Ranger" | "Warden":
            if randAlNum <= 56:
                randAlignment = " [Neutral Evil]"
            elif randAlNum <= 106:
                randAlignment = " [Lawful Evil]"
            elif randAlNum <= 253:
                randAlignment = " [Lawful Neutral]"
            elif randAlNum <= 348:
                randAlignment = " [Chaotic Neutral]"
            elif randAlNum <= 512:
                randAlignment = " [True Neutral]"
            elif randAlNum <= 751:
                randAlignment = " [Neutral Good]"
            else:
                randAlignment = " [Lawful Good]"

        case "Chaos Knight":
            if randAlNum <= 450:
                randAlignment = " [Chaotic Evil]"
            elif randAlNum <= 700:
                randAlignment = " [Chaotic Good]"
            else:
                randAlignment = " [Chaotic Neutral]"

        case _:
            if randAlNum <= 17:
                randAlignment = " [Chaotic Evil]"
            elif randAlNum <= 56:
                randAlignment = " [Neutral Evil]"
            elif randAlNum <= 106:
                randAlignment = " [Lawful Evil]"
            elif randAlNum <= 176:
                randAlignment = " [Chaotic Good]"
            elif randAlNum <= 253:
                randAlignment = " [Lawful Neutral]"
            elif randAlNum <= 348:
                randAlignment = " [Chaotic Neutral]"
            elif randAlNum <= 512:
                randAlignment = " [True Neutral]"
            elif randAlNum <= 751:
                randAlignment = " [Neutral Good]"
            else:
                randAlignment = " [Lawful Good]"

    return randAlignment


def genName(classOption):
    names = name_generator.generate_name
    randName = names()
    genderRoll = 'male' if random.randint(1, 2) == 2 else 'female'

    match classOption:
        case "Elf" | "Half-Elf":
            randName = names(style='elven', library=False, gender=genderRoll)
        case "Dwarf":
            randName = names(style='dwarven', library=False, gender=genderRoll)
        case "Gnome":
            randName = names(style='gnomish', library=False, gender=genderRoll)
        case "Halfling":
            randName = names(style='halfling', library=False, gender=genderRoll)
        case "Gargantua":
            randName = names(style='giant', library=False, gender=genderRoll)
        case "Goblin" | "Half-Orc":
            randName = names(style='orc', library=False, gender=genderRoll)
        case _:
            randName = names(style='human', library=False, gender=genderRoll)

    return randName


def genAttr():
    randAttr1 = GlobalLists.ATTR_LIST[random.randint(1, 292)]
    randAttr2 = GlobalLists.ATTR_LIST[random.randint(1, 292)]
    randAttr3 = GlobalLists.ATTR_LIST[random.randint(1, 292)]

    if randAttr2 == randAttr1: randAttr2 = GlobalLists.ATTR_LIST[random.randint(1, 292)]
    if randAttr3 == randAttr2: randAttr3 = GlobalLists.ATTR_LIST[random.randint(1, 292)]

    randAttrs = " (" + randAttr1 + ", " + randAttr2 + ", " + randAttr3 + ") "

    return randAttrs


def EQLevel(classOption, level):
    eqLevel = 0
    match classOption:
        case "Cleric" | "Fighter" | "Magic User" | "Thief" | "Acrobat" | "Assassin" | "Barbarian" | "Bard" | "Cleric" | \
             "Druid" | "Illusionist" | "Knight" | "Paladin" | "Ranger" | "Arcane Bard" | "Beast Master" | \
             "Chaos Knight" | "Mage" | "Warden" | "Necromancer" | "Acolyte" | "Kineticist" | "Mage" | "Archer" | \
             "Alchemist" | "Merchant":
            if level > 14: eqLevel = 14
        case "Dwarf" | "Half-Elf":
            if level > 12: eqLevel = 12
        case "Elf" | "Drow"| "Changeling" | "Gargantua":
            if level > 10: eqLevel = 10
        case "Halfling" | "Gnome" | "Half-Orc" | "Mutoid" | "Goblin" | "Hephaestan":
            if level > 8: eqLevel = 8
        case "Mycellian":
            if level > 6: eqLevel = 6
        case _:
            eqLevel = 0

    return eqLevel


class RetainerGen:
    retList = []

    def __init__(self, levMax, levMin, amt, extras):
        self.extras = extras
        self.levMax = levMax
        self.levMin = levMin
        self.amt = amt

    def genCLAN(self):
        # Generates a random class, level, alignment, and name
        randLevel = random.randint(self.levMin, self.levMax)
        randClass = self.genClass(randLevel)
        randAli = genAlignment(randClass)
        randName = genName(randClass)
        equalizedLevel = EQLevel(randClass, randLevel)

        randCLAN = "**" + str(randName) + "**, Level " + str(equalizedLevel) + ": " + randClass + randAli
        return randCLAN

    def genClass(self, level):
        if level == 0:
            randClass = "Human"
        else:
            if self.extras:
                randClass = GlobalLists.CLASS_LIST_EXTRAS[random.randint(0, GlobalLists.CLASS_LIST_EXTRAS_LENGTH - 1)]
            else:
                randClass = GlobalLists.CLASS_LIST[random.randint(0, GlobalLists.CLASS_LIST_LENGTH - 1)]

        return randClass

    def genRet(self):
        currCLN = self.genCLAN()
        currAttrs = genAttr()

        currRet = currCLN + currAttrs
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
