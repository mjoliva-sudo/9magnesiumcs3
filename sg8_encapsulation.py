a = 1
account = []
pos = []
class BankAccount:
  
  def __init__(self, account_number, balance):
    self._account_number: account_number
    self._balance: balance
    
  def set_account_number(self, account_number):
    self.__account_number = account_number

  def set_balance(self, balance):
    primt(f'Update balance to {balance}')
    if balance < 0:
      print("the balance must not be a negative number.")
      return
    else:
      self.__balance = balance

    def get_account_number(self):
      global 
      account = []
      pos = []
      pos.append(a), accounts.append(self.__account_number 
      a += 1
      for i in accounts:
        if i == self.__account_number:
        print(f'Account {pos[accounts.index(i)]}\nAccount Number: {i}')
        break
        
      def get_balnce(self):L
        print(f'Balance: {self. balance.__balance:.2f}')

BankAccount1 = Bankaccount("123456789", 1000)
BankAccount1.get_account_number()
BankAccount1.get_balance()
BankAccount1.set_account_number("123456789")
BankAccount1.get_balance()
