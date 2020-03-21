class Item:
    
    def __init__(self, owner, desc, hpGain, atkGain , defGain, menuID):
        
        self.desc = desc
        self.defGain = defGain
        self.atkGain = atkGain
        self.hpGain = hpGain
        self.owner = owner
        self.location = ""
        self.menuID = menuID

    def getMenuID(self):
        return self.menuID

    def setMenuID(self, menuID):
        self.menuID = menuID

    def getLocation(self):
        return self.location

    def setLocation(self, tileObj):
        self.location = tileObj 

    def getName(self):
        return self.desc
    
    def getOwner(self):
        return self.owner
    
    def getName(self):
        return self.desc
    
    def getOwner(self):
        return self.owner

    def setOwner(self, playerObj):
        self.owner = playerObj
        
    def getHpGain(self):
        return self.hpGain

    def setHpGain(self, amt):
        self.hpGain += amt

    def getAtkGain(self):
        return self.atkGain

    def setAtkGain(self, amt):
        self.atkGain += amt

    def getDefGain(self):
        return self.defGain

    def setDefGain(self, amt):
        self.defGain += amt
    
    def used(self, playerObj):
        playerObj.setDefence(self.defGain)
        playerObj.setHealth(self.hpGain)
        playerObj.setAttack(self.atkGain)
        playerObj.setStats(" ".join(["HP: "+str(playerObj.getHealth()),
                                     "ATK: "+str(playerObj.getHealth()),
                                     "DFN: "+str(playerObj.getHealth())]))
        
##        print(playerObj.getName() +
##              " uses " + self.desc)
##        print("+" + str(self.defGain) + " Deffence")
##        print("+" + str(self.hpGain) + " HP")
##        print("+" + str(self.atkGain) + " Attack")
