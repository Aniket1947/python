class student:
    def __init__(self,name):
        self.name=name
        
    
    def __displayinfo(self):
        print("We are learning python")

    def display(self):
       self.__displayinfo()

s=student("Aniket")  
s.display()
# s.__displayinfo()

#################################################################################################################

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f"Depoit Amount:{amount},Total Balance:{self.__balance}")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance =self.__balance - amount
            print(f"Withdraw amount:{amount},Remaining Balance:{self.__balance}")

    def get_balance(self):
        return self.__balance


b=BankAccount(5000)
b.deposit(500)
b.withdraw(200)
print(f"Your main balance is {b.get_balance()}")


#Directly Attemping to change balance
try:
    print(b.__balance)
except Exception as e:
    print(f"Could not access balance directly {e}")






##################################################################################################################

class BankAccount:
    def __init__(self, initial_balance):
        # The balance is a private attribute (by convention)
        # using a double underscore prefix
        self.__balance = initial_balance

    def deposit(self, amount):
        """Method to deposit money with validation."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        """Method to withdraw money with validation."""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}. New Balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")

    def get_balance(self):
        """Getter method to securely access the balance."""
        return self.__balance

# Usage
account = BankAccount(1000)

# Interact with the account using methods (controlled access)
account.deposit(500)
account.withdraw(200)

print(f"Current balance via getter: ${account.get_balance()}")

# Attempting direct access (this is discouraged and will cause an error in most IDEs/linters)
try:
    print(account.__balance)
except AttributeError as e:
    print(f"\nCould not access balance directly: {e}") #

# Attempting unauthorized modification (also prevented)
account.__balance = 1000000 # This creates a new public attribute, it doesn't change the internal one
print(f"Balance after attempted direct modification: ${account.get_balance()}")


