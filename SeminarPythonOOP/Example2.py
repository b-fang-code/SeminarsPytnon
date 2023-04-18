class Example2():

    def __init__(self, x, y, z=0):  # консткуктор
        self.x = x
        self.y = y
        self.z = z
        self.__param = 42


ob2 = Example2(2, 3, 4)
ob3 = Example2(4, 3)
print(ob2.x, ob2.y, ob2.z)
print(ob3.x)
print(ob3._Example2__param)
