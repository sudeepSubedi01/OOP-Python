class Customer:
  def __init__(self,name,gender,address):
    self.name = name
    self.gender = gender
    self.address = address
  
  def edit_customer(self, new_name, new_gender,new_city, new_pincode, new_state):
    self.name = new_name
    self.gender = new_gender
    self.address.edit_address(new_city, new_pincode, new_state)

class Address:
  def __init__(self,city,pincode,state):
    self.city = city
    self.pincode = pincode
    self.state = state

  def edit_address(self, new_city, new_pincode, new_state):
    self.city = new_city
    self.pincode = new_pincode
    self.state = new_state

add = Address('KTM',25693,'HE')
c1 = Customer('Hari','Male',add)

print(c1.address.city)
print(c1.address.pincode)

c1.edit_customer('Sita','Female','Pokhara',45698712,'WE')
print(c1.address.city)