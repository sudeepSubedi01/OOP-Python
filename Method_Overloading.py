class Geometry:
  def area(self,radius):
    return 3.14 * radius * radius
  
  def area(self,l,b):
    return l*b
  
obj = Geometry()
print(obj.area(4,5))
print(obj.area(3.14))

#In python, method overloading does not work.
#The second area function overwrites the first area function.
# Method is not invoked based on the number of arguments
# So method overloading can be achieved in Python logically
