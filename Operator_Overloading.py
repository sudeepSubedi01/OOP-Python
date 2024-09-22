class Concatenate:
  def __init__ (self,string):
    self.string = string

  def __add__(self,other):
    temp = Concatenate('')
    temp.string = self.string + other.string
    return temp


c1 = Concatenate('Hello')
c2 = Concatenate('World')
c3 = c1 + c2
print(c3.string)