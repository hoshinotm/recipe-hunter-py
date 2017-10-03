from appJar import gui

class GUI(gui):

    def __init__(self, label="", color="lightgrey"):
        gui.__init__(self)
        self.app = gui()

    def go(self):
        gui.go(self)

    def setLabel(self, label):
        self.addLabel(self.app,label)

    def setColor(self, color):
        self.app.setColor(self.app,color)

