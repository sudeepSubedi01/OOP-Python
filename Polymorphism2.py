class A:
  def __init__(self):
    self.val1 = 100
  def display1(self,val1):
    print('Class A: ',self.val1)

class B(A):
  def display2(self,val1):
    print('Class B : ',self.val1)

obj = B()
obj.display1(200)
obj.display2(500)