import GlobalLists


class SpellList:
    spellList = []

    def __init__(self, classOption, level):
        self.classOption = classOption
        self.level = level

    def getSpellList(self):
        self.spellList = GlobalLists.MASTER_SPELL_DICT[self.classOption][self.level]

        return self.spellList

    def formatSpellList(self):
        spellString = "(Some spells may not be linked properly as they do not appear in the SRD)\n" + "Level **" + self.level + "** spells for the class of **" + self.classOption + "**:\n"
        for s in self.spellList:
            spellLink = "[" + s + "](<https://oldschoolessentials.necroticgnome.com/srd/index.php/" + s.replace(" ",
                                                                                                                "_") + ">)"
            spellString = spellString + "- " + spellLink + "\n"

        return spellString


class Spell:
    spellLocs = []

    def __init__(self, spellName):
        self.spellName = spellName

    def formatSpell(self):
        newSpell = self.spellName.title()
        newSpell = newSpell.replace(" Of ", " of ")
        newSpell = newSpell.replace(" From ", " from ")
        newSpell = newSpell.replace(" And ", " and ")
        newSpell = newSpell.replace(" With ", " with ")
        self.spellName = newSpell

    def findSpell(self):
        self.spellLocs = []
        j = 0

        for classOpt in GlobalLists.MASTER_SPELL_DICT.values():
            i = 0
            for level in classOpt.values():
                if self.spellName in level:
                    self.spellLocs.append(list(GlobalLists.MASTER_SPELL_DICT)[j] + " at spell level " + str(list(classOpt)[i]))
                i += 1
            j += 1

        return self.spellLocs

    def printSpell(self):
        locString = "These classes can learn the " + self.spellName + " spell:"
        for l in self.spellLocs: locString = locString + "\n- " + l

        return locString
