class Calc:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def multi(self):
        return self.a * self.b


number = Calc(4, 5)
print(number.sum())
print(number.multi())
