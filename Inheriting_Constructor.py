class Phone:
  def __init__(self,price,brand,camera):
    print('Inside Phone Constructor')
    self.price = price
    self.brand = brand
    self.camera = camera
  def buy(self):
    print('Buying a phone')
  def return_phone(self):
    print('Returning phone')
  
class SmartPhone(Phone):
  pass

s1 = SmartPhone(20000,'Apple', 45)
print(s1.camera)
