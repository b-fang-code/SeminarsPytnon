class Example5():
    def __init__(self, x):
        self.x = x

    def getx(self):
        return self.x

    def setx(self, x):
        self.x = x

ob5 = Example5(33)
print(ob5.getx())
ob5.setx(21)
print(ob5.getx())
