class Phone:
  def __init__(self,price,brand,camera):
    print('Inside Phone Constructor')
    self.__price = price
    self.brand = brand
    self.camera = camera

  def buy(self):
    print('Buying a Phone')

class SmartPhone(Phone):
  def buy(self):
    print("Buying a SmartPhone")
    super().buy()

s1 = SmartPhone(56900,"Nokia",89)
print(s1.brand)
s1.buy()
# s1.super().buy()   # doesnt work outside a class