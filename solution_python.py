class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.actionList = []
        self.position = -1


    def add(self, num: int):
        self.value += num
        self.actionList += [("+",num)]
        self.position +=1



    def subtract(self, num: int):
        self.value -= num
        self.actionList += [("-",num)]
        self.position +=1

    def undo(self):
        if (self.position == -1):
            return
        if (self.actionList[self.position][0] == "+"):
            self.value -= self.actionList[self.position][1]
        else:
            self.value += self.actionList[self.position][1]
        self.position -= 1


    def redo(self):
        if (self.position == len(self.actionList) - 1):
            return
        if (self.actionList[self.position+1][0] == "+"):
            self.value += self.actionList[self.position][1]
        else:
            self.value -= self.actionList[self.position][1]
        self.position += 1

    def bulk_undo(self, steps: int):
        for i in range(steps):
            EventSourcer.undo(self)

    def bulk_redo(self, steps: int):
        for i in range(steps):
            EventSourcer.redo(self)
