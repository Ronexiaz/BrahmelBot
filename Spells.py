import GlobalLists

class Spell:
    def __init__(self, classOption, level):
        self.classOption = classOption
        self.level = level

    def getSpellList(self):
        spellList = GlobalLists.MASTER_SPELL_DICT[self.classOption][self.level]

        return spellList
