class Atm:
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
    if(user_input == '1'):
      self.create_pin()
      self.menu()
    elif(user_input == '2'):
      self.deposit()
      self.menu()
    elif(user_input == '3'):
      self.withdraw()
      self.menu()
    elif(user_input == '4'):
      self.check_balance()
      self.menu()
    elif(user_input == '5'):
      self.exit_atm()
  
  def create_pin(self):
    self.pin = input('Enter your new pin: ')
    print('Pin set sucessfully')

  def deposit(self):
    tempPin = input('Enter your pin: ')
    if tempPin == self.pin:
      amount = int(input('Enter amount to deposit: '))
      self.balance = self.balance + amount
      print('Deposited successfully')
    else:
      print('Invalid Pin. Try again!!')
      self.deposit()

  def withdraw(self):
    tempPin = input('Enter your pin: ')
    if tempPin == self.pin:
      amount = int(input('Enter amount to withdraw: '))
      if amount < self.balance:
        self.balance = self.balance - amount
        print('Withdraw successful')
      else:
        print('Insufficient funds')
    else:
      print('Invalid Pin. Try again!!')
      self.withdraw()

  def check_balance(self):
    tempPin = input('Enter you pin: ')
    if tempPin == self.pin:
      print('Your current balance is:' + str(self.balance))
    else:
      print('Invalid Pin. Try again!!')
      self.check_balance()

  def exit_atm(self):
    print('Thank you for using our ATM service')

sbi = Atm()


# For encapsulation:
# Remove self.menu() from __init__ method
# Open python interperter
# python
# from ATM import Atm
# sbi = Atm()
# Try changing the content of the data members from outside the class through that object
# sbi.balance()
# This can easily change the content of the variable. So to prevent this ENCAPSULATION is done.