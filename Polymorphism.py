class Parent:
  def __init__(self,num):
    self.__num = num
  def show_num(self):
    return self.__num
  
class Child(Parent):
  def show(self):
    print("Inside Show Method of Child class")

son = Child(46)
print(son.show_num())
son.show()