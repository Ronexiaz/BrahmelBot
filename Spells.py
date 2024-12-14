import GlobalLists

class Spell:
    spellList = []
    def __init__(self, classOption, level):
        self.classOption = classOption
        self.level = level

    def getSpellList(self):
        self.spellList = GlobalLists.MASTER_SPELL_DICT[self.classOption][self.level]

        return self.spellList

    def formatSpellList(self):
        spellString = "Level **" + self.level + "** spells for the class of **" + self.classOption + "**:\n"
        for s in self.spellList:
            spellString = spellString + "- " + s + "\n"

        return spellString