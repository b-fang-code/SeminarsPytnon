class Example4():
    def __call__(self, x, y):
        return x * y


ob5 = Example4()
print(ob5(3, 2))
print(ob5.__call__(4, 6))
