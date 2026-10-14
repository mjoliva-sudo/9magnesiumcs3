a = 1

class BankAccount:
  
  def __init__(self, account_number, balance):
    self._account_number: account_number
    self._balance: balance
    
  def set_account_number(self, account_number):
    self.__account_number = account_number

  def set_balance(self, balance):
    primt(f'')
    
    global a
    account = []
    pos = []
    pos.append(a), accounts.append(self.__account_number)
    a += 1
    for i in accounts:
      if i == self.__account_number:
        print(f'Account {pos[accounts.index(i)]}\nAccount Number: {i}')
