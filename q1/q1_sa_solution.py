# solution ng summative assessment
class Bank:
  name = ""
  __accounts = []
  
  def __init__(self, name):
    self.name = name
    print("Welcome to", self.name)

  def openAccount(self):
    print("Ready to open an account")
    acc_name = input("Account name: ")
    acc_num = input("Account number: ")
    acc_type = input("Account type (savings or checking): ").lower()
    
    if acc_type == "savings":
      account = SavingsAccount(acc_name, acc_num)
    else:
      account = Account(acc_name, acc_num)
      
    self.__accounts.append(account)
    print("Account created")
    print(account)

  def showAccounts(self):
    print("Showing accounts")
    for a in self.__accounts:
      print(a)

  def deposit(self):
    print("Ready to deposit an amount")
    amount = float(input("Enter amount to deposit: "))
    acc_num = input("Enter account number: ")
    for a in self.__accounts:
      if a.number == acc_num:
        a.deposit(amount)
        print(a)
  
  def addInterest(self):
    print("Adding interest to all savings accounts")
    for a in self.__accounts:
      if isinstance(a, SavingsAccount):
        print("Interest added to account", a.number)
        a.addInterest()
        print(a)
  
  def closeAccount(self):
    print("Ready to close an account")
    acc_num = input("Enter account number: ")
    for a in self.__accounts:
      if a.number == acc_num:
        self.__accounts.remove(a)
        del a
        print("Account closed")

  def __del__(self):
    print("Thank you for banking with", self.name)
    for a in self.__accounts:
      self.__accounts.remove(a)
      del a

  

class Account:
  name = ""
  number = ""
  __balance = 0
  
  def __init__(self, name, number):
    self.name = name
    self.number = number
    
  def deposit(self, amount):
    self.__balance += amount
    
  def withdraw(self, amount):
    if amount > self.__balance:
      print("Insufficient Funds")
    else:
      self.__balance -= amount
      
  def getBalance(self):
    return self.__balance
    
  def __str__(self):
    return self.name + " [" + self.number + "] P" + str(self.__balance)
    
  def __del__(self):
    print("Account ", self.number, " closed")



class SavingsAccount(Account):
  __interest = 0.05
  
  def addInterest(self):
    interestToAdd = super().getBalance() * self.__interest
    super().deposit(interestToAdd)


bank = Bank("Land Bank")
bank.openAccount()
bank.openAccount()
bank.showAccounts()
bank.deposit()
bank.deposit()
bank.addInterest()
bank.closeAccount()
