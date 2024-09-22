class Geometry:
  def area(self,a,b=0):
    if b==0:
      return 3.14 * a**2
    else:
      return a*b
  
obj = Geometry()
print('Area of Rectangle: ', obj.area(4,5))
print('Area of Circle: ', obj.area(10))

# This is still method overloading because same function is doing different task when different number of arguments are passed

