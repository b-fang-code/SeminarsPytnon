
class Car:
    def __init__(self, model:str, color: str, volume: float):
        self.model = model
        self.color = color
        self.volume = volume

    def present(self):
        return f'Это машина {self.model}, {self.color} цвета и объём {self.volume} литра'
    def gas(self):
        print('Бррррбрррр!')


ferrari = Car('F355', 'red', 6.0)
bmw = Car('M3', 'black', 5.0)

print(ferrari.color)
print(bmw.color)
ferrari.gas()
print(ferrari.present())
print(bmw.present())