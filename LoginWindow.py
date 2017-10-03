from recipe_hunter.GUI import GUI

class LoginWindow(GUI):

    def press(self, button):
        if button == "Cancel":
            self.gui.stop()
        else:
            usr = self.gui.getEntry("Username")
            pwd = self.gui.getEntry("Password")
            print("User:", usr, "Pass:", pwd)
            exit(code=1)

    def __init__(self,gui):
        #GUI.__init__(self)
        self.gui = gui
        self.gui.addLabelEntry("Username")
        self.gui.addLabelSecretEntry("Password")
        self.gui.addButtons(["Submit", "Cancel"], self.press)
