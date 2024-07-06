import random
import GlobalLists

class Potion:
    appearance = ""
    taste = ""

    def genPot(self):
        chosenPot = GlobalLists.POT_DICT_LIST[random.randint(1, GlobalLists.POT_COUNT - 1)]
        self.appearance = chosenPot["appearance"]
        self.taste = chosenPot["taste"]

    def getMessage(self):
        self.genPot()
        msgP1 = GlobalLists.BRAHMEL_SAYS_LIST_EXCLAIM[random.randint(1, len(GlobalLists.BRAHMEL_SAYS_LIST_EXCLAIM) - 1)]
        msgP2 = GlobalLists.BRAHMEL_SAYS_LIST_STATE[random.randint(1, len(GlobalLists.BRAHMEL_SAYS_LIST_STATE) - 1)]

        return (msgP1 + msgP2 + "It appears to be a " +
                self.appearance +
                " Also, it " +
                self.taste)

    def getMessages(self, amt):
        msgMain = ""

        for i in range(amt):
            msgMain += "- " + self.getMessage() + "\n"

        return msgMain
