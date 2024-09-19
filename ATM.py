class Atm:
  #constructor
  def __init__(self):
    self.pin = ''
    self.balance = 0
    self.menu()
  def menu(self):
    user_input = input("""
          Hello! How would you like to proceed?
          1. Create Pin
          2. Deposit
          3. Withdraw
          4. Check balance
          5. Exit
    """)
    if(user_input == 1):
      print('Create Pin')
    elif(user_input == 2):
      print('Deposit')
    elif(user_input == 3):
      print('Withdraw')
    elif(user_input == 4):
      print('Check Balance')
    elif(user_input == 5):
      print('Exit')
  
  def create_pin(self):
    self.pin = input('Enter your new pin')
    print('Pin set sucessfully')

  def deposit(self):
    temp = input('Enter your new pin')
    if temp == self.pin:
      amount = int(input('Enter amount to deposit:'))
      self.balance = self.balance + amount
      print('Deposited successfully')
    else:
      print('Invalid Pin')
    