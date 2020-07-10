class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.undoList = []
        self.redoList = []

    def add(self, num: int):
        self.value += num
        self.undoList += [("+",num)]
        print(str(self.undoList) + "  ,  " + str(self.value))
        #self.redoList = []


    def subtract(self, num: int):
        self.value -= num
        self.undoList += [("-",num)]
        #self.redoList = []

    def undo(self):
        if (len(self.undoList) == 0):
            return
        if (self.undoList[-1][0] == "+"):
            self.value -= self.undoList[-1][1]
        else:
            self.value += self.undoList[-1][1]
        self.redoList += self.undoList[-1:]
        del self.undoList[-1]


    def redo(self):
        if (len(self.redoList) == 0):
            return
        if (self.redoList[-1][0] == "+"):
            self.value += self.redoList[-1][1]
        else:
            self.value -= self.redoList[-1][1]
        self.undoList += self.redoList[-1:]
        del self.redoList[-1]

    def bulk_undo(self, steps: int):
        for i in range(steps):
            EventSourcer.undo(self)

    def bulk_redo(self, steps: int):
        for i in range(steps):
            EventSourcer.redo(self)
