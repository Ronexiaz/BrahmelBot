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
            spellLink = "[" + s + "](<https://oldschoolessentials.necroticgnome.com/srd/index.php/" + s.replace(" ", "_") + ">)"
            spellString = spellString + "- " + spellLink + "\n"

        return spellString


class Spell:
    pass
