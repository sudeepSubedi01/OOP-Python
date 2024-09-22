class Complex:
  __counter = 0
  def __init__(self):
    print(id(self))
    self.real = 5
    self.imag = 9
    Complex.__counter +=1
    self.sn = Complex.__counter   #assigning current value of the static variable to the instance variable

  @staticmethod
  def get_counter():
    return Complex.__counter
  
  @staticmethod
  def set_counter(new_count):
    if type(new_count) == int:
      Complex.__counter = new_count
    else:
      print('Invalid Counter value')



# Static variable is a class variable
# Static variable = counter / Complex.counter
# Instance variable = real, imag / self.real, self.imag
# At the very first, class variable is initialized to 0
# Single copy of class variable is shared by all the instances
# Complex.counter is common for all the instances
# c1.Counter = c2.Counter = c3.Counter = Complex.counter
# c1.Counter = 1, c2.Counter = 2 , c3.Counter =3

# Without encapsulation, anyone can change the class variable by Complex.counter = 6, such that c1.Counter = c2.Counter = c3.Counter = Complex.counter = 6
# Class variable can be made private by prefixing by __
# Class variable can be accessed by : Complex._Complex__counter , c1._Complex__counter, c3._Complex__counter
# Class varibale can be modified by : Complex._Complex__counter
# 