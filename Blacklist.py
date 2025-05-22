import dill as pickle

class Blacklist:
    def __init__(self):
        self.blacklistDict = {}

    def addUser(self, userName):
        if userName in self.blacklistDict:
            self.blacklistDict[userName] += 1
        else:
            self.blacklistDict[userName] = 1

    def removeUser(self, userName):
        if userName in self.blacklistDict:
            del self.blacklistDict[userName]
    def getUsersWithCountOverTen(self):
        return {userName: count for userName, count in self.blacklistDict.items() if count > 10}

    def saveToFile(self, filePath='blacklist.pkl'):
        with open(filePath, 'wb') as file:
            pickle.dump(self.blacklistDict, file)

    def loadFromFile(self, filePath='blacklist.pkl'):
        with open(filePath, 'rb') as file:
            self.blacklistDict = pickle.load(file)
    def initialise(self):
        self.loadFromFile()
    def clear(self):
        self.blacklistDict = {}
blacklist = Blacklist()
blacklist.initialise()
blacklist.removeUser('user1')
blacklist.saveToFile()
if __name__ == "__main__":
    blacklist = Blacklist()
    blacklist.loadFromFile()

    print(blacklist.getUsersWithCountOverTen())
    newDict=blacklist.getUsersWithCountOverTen()
    for key,value in blacklist.blacklistDict.items():
        newDict[key]=value
    import HTMLPSR
    html=HTMLPSR.toHTMLDict(newDict,'Blacklist')
    HTMLPSR.openinBrowser(html)

