import random

import GlobalLists


class FullKit:
    def __init__(self, classoption, level):
        self.classoption = classoption
        self.level = level

    def assembleKit(self):
        selfCombatKit = combatKit(self.classoption, self.level)
        selfOtherKit = otherKit(self.classoption, self.level)

        combatKitString = "**PERSON**:\n"
        for equip in selfCombatKit:
            combatKitString += equip + "\n"

        otherKitString = "**BACKPACK**:\n"
        for equip in selfOtherKit:
            otherKitString += equip + "\n"

        fullKitString = combatKitString + "\n" + otherKitString
        return fullKitString


def combatKit(classoption, level):
    kitList = []
    match classoption:
        case 'CLERIC':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[2]))
            if random.randint(1, 2) == 2: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
            kitList.append('Holy Symbol')
        case 'THIEF':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 2) == 2: kitList.append('Leather Armor')
        case 'FIGHTER':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 1: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'DWARF':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[1]))
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'HALFLING':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[1]))
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'ELF':
            kitList.append("Spellbook")
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'MAGIC USER':
            kitList.append("Spellbook")
            if random.randint(1, 2) == 2: kitList.append(chooseRandomFromList(['Dagger', 'Dagger (Silver)']))
        case 'ALCHEMIST':
            if random.randint(1, 2) == 2: kitList.append(chooseRandomFromList(['Dagger', 'Dagger (Silver)', 'Sling\nShot [80]']))
            if random.randint(1, 2) == 2: kitList.append('Leather Armor')
        case 'ILLUSIONIST':
            kitList.append("Spellbook")
            if random.randint(1, 2) == 2: kitList.append(chooseRandomFromList(['Dagger', 'Dagger (Silver)']))
        case 'GNOME':
            kitList.append('Spellbook')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[1]))
            if random.randint(1, 6) > 3: kitList.append('Leather Armor')
            if random.randint(1, 6) > 3: kitList.append('Shield')
        case 'GARGANTUA':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 1: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'WARDEN':
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail']))
        case 'RANGER':
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail']))
            if level >= 8: kitList.append('Holy Symbol')
        case 'ASSASSIN':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 3: kitList.append('Leather Armor')
            if random.randint(1, 6) > 3: kitList.append('Shield')
        case 'ACROBAT':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[3]))
            if random.randint(1, 6) > 3: kitList.append('Leather Armor')
        case 'BEAST MASTER':
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail']))
        case 'GOBLIN':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[1]))
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'NECROMANCER':
            kitList.append('Spellbook')
            if random.randint(1, 2) == 2: kitList.append(chooseRandomFromList(['Dagger', 'Dagger (Silver)', 'Staff']))
        case 'DRUID':
            kitList.append(chooseRandomFromList(['Club', 'Dagger', 'Sling\nShot [80]', 'Spear', 'Staff']))
            if random.randint(1, 6) > 3: kitList.append('Leather Armor')
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append('Holy Symbol')
        case 'MERCHANT':
            if random.randint(1, 2) == 2: kitList.append(chooseRandomFromList(['Dagger', 'Dagger (Silver)', 'Sling\nShot [80]']))
            if random.randint(1, 2) == 2: kitList.append('Leather Armor')
        case 'ARCHER':
            if random.randint(1, 2) == 2: kitList.append(chooseRandomFromList(['Dagger', 'Dagger (Silver)',]))
            kitList.append(chooseRandomFromList(
                ['Crossbow\nBolts [30]', 'Short Bow\nArrows [50]', 'Long Bow\nArrows [50]']))
            if random.randint(1, 2) == 2: kitList.append('Leather Armor')
        case 'ACOLYTE':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[2]))
            kitList.append('Holy Symbol')
            if random.randint(1, 2) == 2: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'HEPHAESTAN':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 2) == 2: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail']))
        case 'KINETICIST':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
        case 'MAGE':
            kitList.append('Scroll (' + chooseRandomFromList(
                ["Charm Person", "Detect Magic", "Floating Disc", "Hold Portal", "Light (Darkness)", "Magic Missile",
                 "Protection from Evil", "Read Languages", "Read Magic", "Shield", "Sleep", "Ventriloquism"]) + ')')
            kitList.append(chooseRandomFromList(['Dagger', 'Dagger (Silver)', 'Short Sword', 'Sword', 'Staff']))
        case 'ARCANE BARD':
            kitList.append('Spellbook')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail']))
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
        case 'CHANGELING':
            kitList.append('Leather Armor')
            if random.randint(1, 2) == 2: kitList.append('Shield')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
        case 'CHAOS KNIGHT':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 1: kitList.append('Shield')
            if level >= 9: kitList.append('Holy Symbol')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'MUTOID':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[1]))
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append('Leather Armor')
        case 'MYCELLIAN':
            kitList.append('Shield')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
        case 'BARBARIAN':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 1: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'BARD':
            if level >= 9: kitList.append('Holy Symbol')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[3]))
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail']))
        case 'HALF-ELF':
            kitList.append('Spellbook')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 1: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'HALF-ORC':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 1: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail']))
        case 'KNIGHT':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 1: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'PALADIN':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 1: kitList.append('Shield')
            if level >= 9: kitList.append('Holy Symbol')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
    return kitList


def otherKit(classoption, level):
    kitList = []
    match classoption:
        case 'CLERIC':
            if random.randint(1, 4) < 4: kitList.append('Holy Water [' + str(random.randint(1, 4)) + ' Vials]')
            if random.randint(1, 10) > 7: kitList.append('Potion of Healing')
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'THIEF':
            if random.randint(1, 6) > 1: kitList.append('Thieves\' Tools')
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'FIGHTER':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'DWARF':
            kitList.append(chooseRandomFromList(['Pick (Mining)', 'Sledgehammer', 'Hammer (Small)']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'HALFLING':
            kitList.append(chooseRandomFromList(['Caltrops [20]', 'Magnifying Glass', 'Hammer (Small)']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'ELF':
            if random.randint(1, 10) > 8: kitList.append("Holy Water [" + str(random.randint(1, 4)) + ' Vials]')
            if random.randint(1, 4) > 2: kitList.append("Scroll Case")
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'MAGIC USER':
            kitList.append(chooseRandomFromList(['Scroll Case', 'Belt Pouch', 'Chalk']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'ALCHEMIST':
            kitList.append(chooseRandomFromList(['Sack (Small)', 'Belt Pouch', 'Quill', 'Vial (Glass)']))
            kitList.append(chooseRandomFromList(['Chalk', 'Ink (Vial)', 'Wolfsbane (Bunch)']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'ILLUSIONIST':
            kitList.append(chooseRandomFromList(['Scroll Case', 'Belt Pouch', 'Chalk']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'GNOME':
            kitList.append(chooseRandomFromList(['Caltrops [20]', 'Magnifying Glass', 'Marbles [20]']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'GARGANTUA':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'WARDEN':
            kitList.append(chooseRandomFromList(['Wolfsbane (Bunch)', 'Lantern', 'Tent']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'RANGER':
            kitList.append(chooseRandomFromList(['Wolfsbane (Bunch)', 'Lantern', 'Tent']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'ASSASSIN':
            kitList.append(chooseRandomFromList(['Caltrops [20]', 'Manacles', 'Chain [10 Feet]']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'ACROBAT':
            kitList.append(chooseRandomFromList(['Pole (Wooden, 10\')', 'Rope [50 Feet]', 'Twine [100 Feet]']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'BEAST MASTER':
            kitList.append(chooseRandomFromList(['Wolfsbane (Bunch)', 'Lantern', 'Tent']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'GOBLIN':
            kitList.append(chooseRandomFromList(['Caltrops [20]', 'Manacles', 'Chain [10 Feet]']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'NECROMANCER':
            kitList.append(chooseRandomFromList(['Scroll Case', 'Belt Pouch', 'Chalk']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'DRUID':
            kitList.append(chooseRandomFromList(['Wolfsbane (Bunch)', 'Lantern', 'Tent']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'MERCHANT':
            kitList.append(chooseRandomFromList(['Pole (Wooden, 10\')', 'Rope [50 Feet]', 'Twine [100 Feet]']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'ARCHER':
            kitList.append(chooseRandomFromList(['Pole (Wooden, 10\')', 'Rope [50 Feet]', 'Twine [100 Feet]']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'ACOLYTE':
            if random.randint(1, 4) < 4: kitList.append('Holy Water [' + str(random.randint(1, 4)) + ' Vials]')
            if random.randint(1, 10) > 7: kitList.append('Potion of Healing')
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'HEPHAESTAN':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'KINETICIST':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'MAGE':
            kitList.append('Ink (Vial)')
            kitList.append('Quill')
            kitList.append('Parchment [2 Sheets]')
            for item in getMiscItems(level * 2): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'ARCANE BARD':
            kitList.append(chooseRandomFromList(['Instrument (Wind)', 'Instrument (String)']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'CHANGELING':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'CHAOS KNIGHT':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'MUTOID':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'MYCELLIAN':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'BARBARIAN':
            kitList.append(chooseRandomFromList(['Wolfsbane (Bunch)', 'Lantern', 'Tent']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'BARD':
            kitList.append(chooseRandomFromList(['Instrument (Wind)', 'Instrument (String)']))
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'HALF-ELF':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'HALF-ORC':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'KNIGHT':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
        case 'PALADIN':
            for item in getMiscItems(level): kitList.append(item)
            kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
    return kitList


def getMiscItems(level):
    kitList = []
    sampleNum = random.randint(1, 6) + (level % 3)
    samples = random.sample(range(1, len(GlobalLists.MISC_ITEM_LIST) - 1), sampleNum)
    for item in samples: kitList.append(GlobalLists.MISC_ITEM_LIST[item])
    return kitList


def chooseRandomFromList(givenList):
    randPick = random.randint(0, len(givenList) - 1)
    return givenList[randPick]


def goldCalc(level):
    goldCt = random.randint(1, (level % 5) + 6) * (2 + (level % 5))
    return goldCt
