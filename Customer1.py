# pass by reference logic
class Customer:
  def __init__(self,name):
    self.name = name

def greet(c2):
  print(id(c2))
  c2.name = 'Hello world'

c1 = Customer('HariLal') 
print(id(c1))
greet(c1)
print(c1.name)




# Line 8: Customer('HariLal') creates a new instance (object) of the Customer class, and the reference variable c1 is used to point to this object in memory.
#         c1 is not the actual object, rather its a reference to the memory location where the Customer object is stored.
# id(c1) gives the memory address (or identifier) where the object c1 is stored.
# When you call greet(c1), you are passing c1 (the reference variable) to the function
# So,c1 refers to an object of class Customer. Inside the function, the parameter c2 receives the same reference to the object that c1 refers to.
# greet() function receives c1 by reference. So, c2 also points to the same object in the memory that c1 refers.
# Both c1 and c2 refer to the same object and hence store the same address.
# Objects, Dictionary and List are mutable. Passing them to a function is pass by reference and hence changes can be made to it from inside the function.

