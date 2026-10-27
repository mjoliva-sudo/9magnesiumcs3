
class BankAccount: # Creation of Class

    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private account number
        self.__balance = balance  # Private balance

    
    def set_account_number(self, account_number): #to update the account number
        self.__account_number = account_number  #Save the new account number

   
    def set_balance(self, balance):  #To update the balance
        if balance < 0:  # Checks if the new balance is negative
            print("The balance must not be a negative number.")  # warning
        else:
            self.__balance = balance  # Updates the balance if it is not negative

    # @property is used to access the account number like an attribute
    @property
    def get_account_number(self):
        return self.__account_number  # Returns the private account number

    # @property is used to access the account balance like an attribute
    @property
    def get_balance(self):
        return self.__balance  # Return the private balance


# Create an object named a1 with account number 12345 and balance 1000
a1 = BankAccount(12345, 1000)

# Display the account information
print("Account 1")
print(f"Account Number: {a1.get_account_number}")  # Display account number
print(f"Balance: {a1.get_balance:.2f}")  # Displays the balance with 2 decimal points