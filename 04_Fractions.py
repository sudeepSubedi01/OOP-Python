class Fraction:
  def __init__(self,n,d):
    self.num = n
    self.den = d

  # def __str__(self):
  #   return 'Hello'

  def __str__(self):      #magic/dunder method in python , called when we try to print the object of the class
    return '{}/{}'.format(self.num,self.den)
  
  # def __add__(self,other):
  #   temp_num = self.num * other.den + other.num * self.den
  #   temp_den = self.den * other.den
  #   return '{}/{}'.format(temp_num,temp_den)

  def __add__(self,other):
    temp = Fraction(0,0)
    temp.num = self.num * other.den + other.num * self.den
    temp.den = self.den * other.den
    return temp
  
  def __sub__(self,other):
    temp = Fraction(0,0)
    temp.num = self.num * other.den - other.num * self.den
    temp.den = self.den * other.den
    return temp
  
  def __mul__(self,other):
    temp = Fraction(0,0)
    temp.num = self.num * other.num
    temp.den = self.den * other.den
    return temp

  def __truediv__(self,other):
    temp = Fraction(0,0)
    temp.num = self.num * other.den
    temp.den = self.den * other.num
    return temp
  
x = Fraction(4,5)
y = Fraction(50,5)
print(type(x))    # <class '__main__.Fraction'>     #This indicates that x is an instance of the Fraction class.
print(x)
print(y)
#By default, printing an object shows a string representation of the object. Since we haven't defined a __str__ or __repr__ method in the Fraction class, Python uses the default representation, which typically looks like: <__main__.Fraction object at 0x...>
#But if there is a dunder method __str__ or __repr__, then the value or string returned by this method is printed

# print(x+y)
sum = x+y
print(sum)

# print(x-y)
diff = x-y
print(diff)

# print(x*y)
product = x*y
print(product)

# print(x/y)
division = x / y
print(division)

