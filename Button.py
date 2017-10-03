from appJar import gui

class Button(object):
    def __init__(self,title="",handler=None):
        self.title = title
        self.handler = handler

    def set_handler(self, handler):
        self.handler = handler

