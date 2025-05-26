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
        case 'CLERIC' | 'ACOLYTE':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[2]))
            if random.randint(1, 2) == 2: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
            kitList.append('Holy Symbol')
        case 'THIEF':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 2) == 2: kitList.append('Leather Armor')
        case 'FIGHTER' | 'GARGANTUA' | 'HALF-ORC' | 'KNIGHT' | 'BARBARIAN':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 1: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'DWARF' | 'HALFLING' | 'GOBLIN':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[1]))
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'ELF' | 'HALF-ELF':
            kitList.append("Spellbook")
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail', 'Plate Mail']))
        case 'MAGIC USER' | 'ILLUSIONIST' | 'NECROMANCER':
            kitList.append("Spellbook")
            if random.randint(1, 2) == 2: kitList.append(chooseRandomFromList(['Dagger', 'Dagger (Silver)']))
        case 'ALCHEMIST':
            if random.randint(1, 2) == 2: kitList.append(chooseRandomFromList(['Dagger', 'Dagger (Silver)', 'Sling\nShot [80]']))
            if random.randint(1, 2) == 2: kitList.append('Leather Armor')
        case 'GNOME':
            kitList.append('Spellbook')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[1]))
            if random.randint(1, 6) > 3: kitList.append('Leather Armor')
            if random.randint(1, 6) > 3: kitList.append('Shield')
        case 'WARDEN' | 'BEAST MASTER':
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail']))
        case 'RANGER':
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail']))
            if level >= 8: kitList.append('Holy Symbol')
        case 'ASSASSIN' | 'CHANGELING':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[0]))
            if random.randint(1, 6) > 3: kitList.append('Leather Armor')
            if random.randint(1, 6) > 3: kitList.append('Shield')
        case 'ACROBAT' | 'MERCHANT':
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[3]))
            if random.randint(1, 6) > 3: kitList.append('Leather Armor')
        case 'DRUID':
            kitList.append(chooseRandomFromList(['Club', 'Dagger', 'Sling\nShot [80]', 'Spear', 'Staff']))
            if random.randint(1, 6) > 3: kitList.append('Leather Armor')
            if random.randint(1, 6) > 3: kitList.append('Shield')
            kitList.append('Holy Symbol')
        case 'ARCHER':
            if random.randint(1, 2) == 2: kitList.append(chooseRandomFromList(['Dagger', 'Dagger (Silver)',]))
            kitList.append(chooseRandomFromList(
                ['Crossbow\nBolts [30]', 'Short Bow\nArrows [50]', 'Long Bow\nArrows [50]']))
            if random.randint(1, 2) == 2: kitList.append('Leather Armor')
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
        case 'CHAOS KNIGHT' | 'PALADIN':
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
        case 'BARD':
            if level >= 9: kitList.append('Holy Symbol')
            kitList.append(chooseRandomFromList(GlobalLists.WEAPON_ITEM_LIST[3]))
            kitList.append(chooseRandomFromList(['Leather Armor', 'Chainmail']))
    return kitList


def otherKit(classoption, level):
    kitList = []
    if classoption == 'MERCHANT': kitList.append('Gold Piece(s) [' + str(goldCalc(level) * ((level % 3) + 2)) + ']')
    else: kitList.append('Gold Piece(s) [' + str(goldCalc(level)) + ']')
    for item in getMiscItems(level): kitList.append(item)
    match classoption:
        case 'CLERIC' | 'ACOLYTE':
            if random.randint(1, 4) > 1: kitList.append('Holy Water [' + str(random.randint(1, 4)) + ' Vials]')
            if random.randint(1, 10) > 7: kitList.append('Potion of Healing')
        case 'THIEF':
            if random.randint(1, 6) > 1: kitList.append('Thieves\' Tools')
            kitList.append(chooseRandomFromList(['Caltrops [20]', 'Manacles', 'Chain [10 Feet]']))
            kitList.append(chooseRandomFromList(['Pole (Wooden, 10\')', 'Rope [50 Feet]', 'Twine [100 Feet]']))
        case 'FIGHTER' | 'HEPHAESTAN' | 'KINETICIST' | 'CHANGELING' | 'CHAOS KNIGHT' \
             | 'MUTOID' | 'MYCELLIAN' | 'HALF-ORC' | 'KNIGHT' | 'PALADIN' | 'GARGANTUA':
            kitList.append('Torches [6]')
            kitList.append(chooseRandomFromList(['Oil [1 Flask]', 'Crowbar', 'Grappling Hook']))
        case 'DWARF':
            kitList.append(chooseRandomFromList(['Pick (Mining)', 'Sledgehammer', 'Hammer (Small)']))
            kitList.append(chooseRandomFromList(['Oil [1 Flask]', 'Crowbar', 'Grappling Hook']))
        case 'HALFLING' | 'GNOME':
            kitList.append(chooseRandomFromList(['Caltrops [20]', 'Magnifying Glass', 'Hammer (Small)', 'Marbles [20]']))
            kitList.append(chooseRandomFromList(['Oil [1 Flask]', 'Crowbar', 'Grappling Hook']))
        case 'MAGIC USER' | 'ELF' | 'HALF-ELF' | 'ILLUSIONIST' | 'NECROMANCER':
            kitList.append(chooseRandomFromList(['Scroll Case', 'Belt Pouch', 'Chalk [10 Sticks]']))
            kitList.append(chooseRandomFromList(['Candles [10]', 'Mirror (Hand-sized, Steel)']))
        case 'ALCHEMIST':
            if random.randint(1, 4) > 3: kitList.append('Holy Water [' + str(random.randint(1, 4)) + ' Vials]')
            kitList.append(chooseRandomFromList(['Sack (Small)', 'Belt Pouch', 'Quill', 'Vial (Glass)']))
            kitList.append(chooseRandomFromList(['Chalk [10 Sticks]', 'Ink (Vial)', 'Wolfsbane (Bunch)']))
        case 'WARDEN' | 'RANGER' | 'BEAST MASTER' | 'DRUID' | 'BARBARIAN':
            kitList.append(chooseRandomFromList(['Wolfsbane (Bunch)', 'Lantern', 'Tent']))
        case 'ASSASSIN' | 'GOBLIN':
            kitList.append(chooseRandomFromList(['Caltrops [20]', 'Manacles', 'Chain [10 Feet]']))
            kitList.append(chooseRandomFromList(['Pole (Wooden, 10\')', 'Rope [50 Feet]', 'Twine [100 Feet]']))
        case 'ACROBAT' | 'ARCHER' | 'MERCHANT':
            kitList.append(chooseRandomFromList(['Pole (Wooden, 10\')', 'Rope [50 Feet]', 'Twine [100 Feet]']))
            kitList.append(chooseRandomFromList(['Caltrops [20]', 'Marbles [20]']))
        case 'MAGE':
            kitList.append('Ink (Vial)')
            kitList.append('Quill')
            kitList.append('Parchment [2 Sheets]')
            for item in getMiscItems(level): kitList.append(item)
        case 'ARCANE BARD' | 'BARD':
            kitList.append(chooseRandomFromList(['Instrument (Wind)', 'Instrument (String)']))
            kitList.append(chooseRandomFromList(['Pole (Wooden, 10\')', 'Rope [50 Feet]', 'Twine [100 Feet]']))
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
