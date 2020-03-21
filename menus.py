class Menu:

    def __init__(self, name ,text ,option, menuID):
        self.name = name
        self.text = text
        self.option = option
        self.menuID = menuID

    def getMenuID(self):
        return self.menuID

    def setMenuID(self, menuID):
        self.menuID = menuID

    def getName(self):
        return self.name

    def getText(self):
        return self.text

    def getOption(self):
        return self.option

    def setName(name):
        self.name = name

    def setText(text):
        self.text = text

    def setOption(option):
        self.option = option
