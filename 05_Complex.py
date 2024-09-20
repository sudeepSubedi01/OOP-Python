class Complex:
  def __init__(self,r,i):
    self.real = r
    self.imag = i
  def __str__(self):
    return '{}+{}i'.format(self.real,self.imag)
  
  def __add__(self,other):
    temp = Complex(0,0)
    temp.real = self.real + other.real
    temp.imag = self.imag + other.imag
    return temp
  
  def __mul__(self,other):
    temp = Complex(0,0)
    temp.real = self.real * other.real - self.imag * other.imag
    temp.imag = self.real * other.imag + self.imag * other.real
    return temp
  
  def __truediv__(self,other):
    temp = Complex(0,0)
    temp.real = (self.real * other.real + self.imag * other.imag) / (other.real **2 + other.imag **2)
    temp.imag = (self.imag * other.real - self.real * other.imag) / (other.real **2 + other.imag **2)
    return temp

c1 = Complex(5,6)
print(c1)
c2 = Complex(1,3)
print(c2)
add = c1 + c2
print(add)
prod = c1 * c2
print(prod)
div = c1 / c2
print(div)
