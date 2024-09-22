class Phone:
  def __init__(self,price,brand,camera):
    print('Inside Phone Constructor')
    self.price = price
    self.__brand = brand
    self.camera = camera
    print(self.__brand)   # value is assigned
  def buy(self):
    print('Buying a phone')
  def return_phone(self):
    print('Returning phone')
  
class SmartPhone(Phone):
  pass

s1 = SmartPhone(20000,'Apple', 45)
print(s1.camera)
# print(s1.brand)           # private members cant be accessed
# print(s1.__brand)         # private members cant be accessed
# print(s1._Phone__brand)   # private members cant be accessed


