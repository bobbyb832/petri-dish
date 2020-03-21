import random
class Player:

    def __init__(self,
                 name,
                 health,
                 attack,
                 defence,
                 inv,
                 isAi,
                 size,
                 color,
                 shape,
                 posX,
                 posY,
                 cRange,
                 stamina,
##                 slots,
                 menuID,
                 speed,
                 team):

        self.turn = 0
        self.team = team
        self.speed = speed
        self.shape = shape
        self.color = color
        self.size = size
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence
        self.inv = []
        self.isAi = True
        self.posX = posX
        self.posY = posY
        self.menuID = menuID
        self.cRange = cRange
        self.stamina = stamina
        self.stats = " ".join(["HP: "+str(self.health), "ATK: "+str(self.attack), "DFN: "+str(self.defence)])
        self.attackList = []
        self.startPos = (posX,posY)
        self.trail = [(posX,posY)]
        self.master = True
##        self.slots = {"weapon":"",
##                      "armer":{"head":"",
##                               "neck":"",
##                               "shoulders":"",
##                               "hands":"",
##                               "torso":"",
##                               "belt":"",
##                               "legs":"",
##                               "shoos":""},
##                      "throwable":"",
##                      "utility":""}

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def getStartPos(self):
        return self.startPos

    def getTrail(self):
        return self.trail

    def setTrail(self, trail):
        self.trail = trail

    def setStartpos(self, startPos):
        self.startPos = startPos

    def setTrail(self,trail):
        self.trail = trail

    def getAttackList(self):
        return self.attackList

    def setAttackList(self, attackList):
        self.attackList = attackList

    def getStamina(self):
        return self.stamina

    def setStamina(self, stamina):
        self.stamina = stamina  

    def getCRange(self):
        return self.cRange

    def setCRange(self, cRange):
        self.cRange = cRange    
    
    def getStats(self):
        return self.stats
    
    def setStats(self, stats):
        self.stats = stats
    
    def getMenuID(self):
        return self.menuID

    def setMenuID(self, menuID):
        self.menuID = menuID

    def getPosX(self):
        return self.posX

    def setPosX(self, posX):
        self.posX = posX
        
    def getPosY(self):
        return self.posY

    def setPosY(self, posY):
        self.posY = posY

    def getTile(self):
        return self.tile

    def setTile(self, symbol):
        self.tile = tile

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, symbol):
        self.symbol = symbol
        self.menuID = symbol
    
    def getChoice(self):
        return self.choice

    def setChoice(self, choice):
        self.choice = choice
        
    def getIsAi(self):
        return self.isAi

    def setIsAi(self, booll):
        self.isAi = booll

    def getShape(self):
        return self.shape

    def getColor(self):
        return self.color

    def getSize(self):
        return self.size

    def setShape(self):
        self.shape = shape

    def setColor(self, color):
        self.color = color

    def setSize(self):
        self.size = size        

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name    

    def getHealth(self):
        return self.health

    def setHealth(self, amt):
        self.health += amt
                
    def getAttack(self):
        return self.attack

    def setAttack(self, amt):
        self.attack += amt

    def getDefence(self):
        return self.defence

    def setDefence(self, amt):
        self.defence += amt

    def getInv(self):
        return self.inv

    def setInv(self, itemObj):
        self.inv.append(itemObj)

    def getTeam(self):
        return self.team

    def setTeam(self, team):
        self.team = team
        

#actions
    def ding(self):
        #if self.master == True:
            
        option = random.randint(1,6)
        self.health += 5
        self.size += .1
        if option == 1:
            self.attack += 5
        if option == 2:
            self.defence += 5
        if option == 3:
            self.health += 10
        if option == 4:
            self.cRange += 5
        if option == 5:
            self.speed += 5


        
        
            
    def strike(self, playerObj):
        if self.team:
            if playerObj.team == self.team:
                pass
                print('on team')
            else:
                playerObj.getHit(self.getAttack())
            
            
            
            
            #self.speed = self.speed + playerObj.getSpeed() + 5
            #self.cRange = self.size
##        print(
##            self.name +
##            " hits " +
##            playerObj.getName() +
##            " for " + str((self.getAttack()) * (playerObj.getDefence()/10)))

    
        
        
            
        
        
    def updateStats(self):
        self.setStats(" ".join(["HP: "+str(self.health),
                           "ATK: "+str(self.attack),
                           "DFN: "+str(self.defence)]))

    def getHit(self, amt):
        self.setHealth(-(amt) * (self.getDefence()/10))
        self.updateStats()

    def useItem(self, itemObj):
        
        if itemObj.getOwner().getName() == self.getName():
            itemObj.used(self)
            self.setInv(self.getInv().remove(itemObj))
            self.inv = list(filter(None ,self.getInv()))
            self.updateStats()

        else:
            print("This is not yours")

       
