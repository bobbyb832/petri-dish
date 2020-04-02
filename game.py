#imports
import pygame
import random
from players import Player
from items import Item
from menus import Menu
import math

#globals
Clock = pygame.time.Clock()
background_colour = (0,0,0)
gridSizeX = round(1920*.25)
gridSizeY = round(1080*.25)
playerSize = 1
pop = 5
(width, height) = (gridSizeX, gridSizeY)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Gladiator')
pygame.display.flip()
directionCharList = ["N","S","E","W","SW","SE","NW","NE"]
firstMenu = ["MOVE","ATTACK","INVENTORY"]

playerList = []

#helpers

#calculates ditance between two objs
def calcDistance(obj1,obj2):
    obj1_X = obj1.getPosX()
    obj1_Y = obj1.getPosY()
    obj2_X = obj2.getPosX()
    obj2_Y = obj2.getPosY()
    distance = math.sqrt(((obj1_X-obj2_X)**2)+((obj1_Y-obj2_Y)**2))
    return round(distance)

#returns other players that are within range to attack
def genAttackList(playerObj,playerList):
    attackList = []
    for i in playerList:
        if i.team == playerObj.team:
            pass
        else:
            if calcDistance(playerObj,i) <= playerObj.getCRange():
                if i.getMenuID() != playerObj.getMenuID():
                    attackList.append(i)

    
    playerObj.setAttackList(attackList)



#gen a random number
def randomGen(beg,end):
    
    a = list(range(beg,end))
    random.shuffle(a)
    return a[random.randint(0,len(a)-1)]

#gen a list of unique random numbers
def uniqueRandGen(beg,end,size):
    numCache = []
    while len(numCache) < size:
        a = randomGen(beg,end)
        while a in numCache:
            a = randomGen(beg,end)
        numCache.append(a)
    return numCache

#gen a list of unique coordinate pairs
def uniqueCoords(beg,sizeX,sizeY,size):
    coordList = []
    compX = 0
    compY = 0
    while len(coordList) < size:
        a = [randomGen(beg+compX,sizeX-compX),randomGen(beg+compY,sizeY-compY)]
        while a in coordList:
            a = [randomGen(beg+compX,sizeX-compX),randomGen(beg+compY,sizeY-compY)]
        coordList.append(a)
    print(coordList)
    return coordList

#generate random RGB values returns as tupel
def randomColors():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#generates all the players
def genPlayers(gridSizeX,gridSizeY, population, begStats):
    playerList = []
    coords = uniqueCoords(0,gridSizeX-1,gridSizeY-1,population)
    
    for i in range(population):
         p = Player("NPC " + str(i + 1),
             10,
             begStats,
             begStats,
             [],
             True,
             playerSize,
             randomColors(),
             '',
             coords[i][0],
             coords[i][1],
             playerSize,
             5,
             "NPC " + str(i + 1),
             5,
             i)
         playerList.append(p)

    return playerList

#generate items (stat boosters)
def genItems(amount):
    a = [Item("No One", "Item " + str(i), 100, 100 , 100, "Item " + str(i)) for i in range(1,amount)]
    return a

#generate a logical grid to be placed over pixels
def genLogicalGrid(gridSizeX,gridSizeY):
    
    sizeX = range(gridSizeX)
    sizeY = range(gridSizeY)
    return [[str(i) for i in sizeY] for j in sizeX]

#generate
def genMenu(optList):
    return [Menu(i,i,i,i) for i in optList]

#register item with an owner(player obj)
def assignItem(playerObj, itemObj):
    playerObj.setInv(itemObj)
    itemObj.setOwner(playerObj)

#turns object properties into a python dictionary
def toDict(obj):
    return obj.__dict__

#print menu id of a menu obj
def printObj(obj):
    
    print(obj.getMenuID())

#prints objects in given object list
def printObjs(objList):
    [printObj(i) for i in objList]


#changes player obj position based on given direction, and steps(pixels)
def movePlayer(playerObj, direction, steps):
    
    x = playerObj.getPosX()
    y = playerObj.getPosY()
    
    if direction == "N":
        playerObj.setPosY(y - steps)
    if direction == "S":
        playerObj.setPosY(y + steps)
    if direction == "W":
        playerObj.setPosX(x - steps)
    if direction == "E":
        playerObj.setPosX(x + steps)
    if direction == "NW":
        playerObj.setPosY(y - steps)
        playerObj.setPosX(x - steps)
    if direction == "NE":
        playerObj.setPosY(y - steps)
        playerObj.setPosX(x + steps)
    if direction == "SW":
        playerObj.setPosY(y + steps)
        playerObj.setPosX(x - steps)
    if direction == "SE":
        playerObj.setPosY(y + steps)
        playerObj.setPosX(x + steps)



#checks to see if the player objs hitpoints are <= 0 
def deathCheck(playerList):
    playerList = playerList
    #print('popSize: ' + str(len(playerList)))
    for player in playerList:
        #print(player)
        if player.getHealth() <= 0:
            
            playerTrail = player.trail
            playerColor = player.color
            pygame.draw.lines(screen, playerColor,False,playerTrail)

##            if player.master == False:
            playerList.remove(player)
            
            
    return playerList


#levels up player object, increases stats

def ding(playerObj):
    #if self.master == True:
        
    option = random.randint(1,5)
    playerObj.health += 5
    playerObj.size += .1
    if option == 1:
        playerObj.attack += 5
    if option == 2:
        playerObj.defence += 5
    if option == 3:
        playerObj.health += 10
    if option == 4:
        playerObj.cRange += 5
    if option == 5:
        playerObj.speed += 5

        
#handles the players choice, runs appropriate function
def choiceHandler(choice,playerObj):
    
    
    if choice.getMenuID() == "MOVE":
        if playerObj.getIsAi() == False:
            moveChoice = optionPrompt(genMenu(possibleDirChoices(playerObj))).getMenuID()
        else:
            a = possibleDirChoices(playerObj)
            ind = randomGen(0,len(a))
            moveChoice = a[ind-1]
        movePlayer(playerObj, moveChoice, playerObj.speed)
        
    if choice.getMenuID() == "ATTACK":
        
        atkList = playerObj.getAttackList()
        if len(atkList) > 0:

            ind = randomGen(0,len(atkList))
            attackChoice = atkList[ind-1]
            playerObj.strike(attackChoice)
            
            if attackChoice.health < 1:
                ding(playerObj)
        else:
            pass
        
    if choice.getMenuID() == "INVENTORY":
        invList = playerObj.getInv()
        if len(invList) > 0:
            if playerObj.getIsAi() == False:
                invChoice = optionPrompt(invList)
            else:
                ind = randomGen(0,len(invList))
                invChoice = invList[ind-1]
            playerObj.useItem(invChoice)
        else:
            pass
        
    playerObj.turn += 1
##    if playerObj.turn % 250 == 0:
##        playerObj.ding()

#prevents player from choosing to go out of bounds
def possibleDirChoices(playerObj):
    Choices = []
    playerX = playerObj.getPosX()
    playerY = playerObj.getPosY()
    if playerX > 0:
        Choices.append("W")
    if playerX < gridSizeX - 1:
        Choices.append("E")
    if playerY > 0:
        Choices.append("N")
    if playerY < gridSizeY - 1:
        Choices.append("S")
    if playerX > 0 and playerY > 0:
        Choices.append("NW")
    if playerX < gridSizeX-1 and playerY < gridSizeY-1:
        Choices.append("SE")
    if playerX > 0 and playerY < gridSizeY-1:
        Choices.append("SW")
    if playerX < gridSizeX-1 and playerY > 0:
        Choices.append("NE")

        
    return Choices


#returns player obj sets it to parent objs team
def addPlayer(parentObj):
    recruit = Player("Child of " + parentObj.name,
             parentObj.health,
             parentObj.attack,
             parentObj.defence,
             [],
             True,
             round(parentObj.size),
             parentObj.color,
             '',
             parentObj.posX,
             parentObj.posY,
             round(parentObj.size),
             5,
             "Child of " + parentObj.name,
             round(parentObj.speed),
             parentObj.team)

    return recruit
    
#main game function
def initGame(mapSizeX,mapSizeY,population,startingStats):
    logGrid = genLogicalGrid(mapSizeX,mapSizeY)
    playerList = genPlayers(mapSizeX,mapSizeY, population, startingStats)
##    for player in playerList:
##        items = genItems(10)
##        for item in items:
##            assignItem(player, item)
    screenFill = (0,0,0)
    while True:
        
        screen.fill(screenFill)
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONUP:
                playerList = genPlayers(mapSizeX,mapSizeY, population, startingStats)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    screenFill = (255,255,255)
                if event.key == pygame.K_DOWN:
                    screenFill = (0,0,0)
                if event.key == pygame.K_RIGHT:
                    for i in playerList:
                        print(i.name + ':' + str(i.team))
                    
            
            if event.type == pygame.QUIT:
                exit()
                running = False

        for i in playerList:
            
            #print(i.name + ':' + str(i.team))
            begMenu = genMenu(firstMenu)
            genAttackList(i,playerList)
            
            if i.getIsAi() == False:
                
                choice = optionPrompt(begMenu)
                choiceHandler(choice,i)
                    
            else:
                
                ind = randomGen(0,len(begMenu))
                choiceHandler(begMenu[ind-1],i)
                pygame.draw.circle(screen,i.color,(i.posX,i.posY),int(i.size))
                i.trail.append((i.posX,i.posY))
                
                pygame.draw.lines(screen, i.color,False,i.trail,1)

                if i.turn % 500 == 0:
                    playerList.append(addPlayer(i))
                    
               
##        if len(playerList) == 1:
##            
##            pygame.display.update()
##            playerList = genPlayers(mapSizeX,mapSizeY, population, startingStats)
##
        playerList = deathCheck(playerList)
        pygame.display.update()
        screen.fill(screenFill)
        Clock.tick(120)
  
            
initGame(gridSizeX,gridSizeY,pop,5)
