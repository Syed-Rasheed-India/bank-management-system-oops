
from models.saving_account import SavingAccount
from models.current_account import CurrentAccount
class BankService:
    
    services ={1: "Create Saving Account", 2: "Create Current Account", 3: "Withdraw Money", 4: "Deposit Money", 5: "Transaction History", 6: "Exit"}
    __saving_account_holders = []
    __current_account_holders = []
    
    def isAccountExists(self,accountNumber,accountHolderName,accountType):
        if accountType.lower() == "saving":
            for account in self.__saving_account_holders:
                if account.accountNumber == accountNumber and account.accountHolderName == accountHolderName:
                    return True
        elif accountType.lower() == "current":
            for account in self.__current_account_holders:
                if account.accountNumber == accountNumber and account.accountHolderName == accountHolderName:
                    return True
        return False
    
    def getDetils(self):

        accountHolderName = input("Enter account holder name: ")
        phoneNumber = input("Enter phone number: ")
        address = input("Enter address: ")
        return accountHolderName, phoneNumber, address
    
    def deposit_money(self,account= None,amount=None):
        if account and amount:
            account.balance += amount
            print(f"Deposited {amount} successfully. Your Account Number is {account.accountNumber}. New balance is {account.balance}")
            return True
        return False

    def create_saving_account(self):
        
        accountHolderName, phoneNumber, address = self.getDetils()
        
        saving_account = SavingAccount(accountHolderName, phoneNumber, address)
        
        if saving_account.balance < saving_account.minimumBalance:
            print(f"Minimum balance of {saving_account.minimumBalance} is required. so Please deposit money to create account")
            amt = float(input("Enter amount to deposit: "))
            if amt > saving_account.minimumBalance:
                if self.deposit_money(saving_account,amt):
                    self.__saving_account_holders.append(saving_account)
                    print("Account created successfully!")
                
                else:
                    print("Account creation failed!")
            else:
                print(f"Amount should be greater than minimum balance of {saving_account.minimumBalance}")
    def create_current_account(self):
        accountHolderName, phoneNumber, address = self.getDetils()
        
        current_account = CurrentAccount(accountHolderName, phoneNumber, address)
        
        if current_account.balance < current_account.minimumBalance:
            print(f"Minimum balance of {current_account.minimumBalance} is required. so Please deposit money to create account")
            amt = float(input("Enter amount to deposit: "))
            if amt > current_account.minimumBalance:
                if self.deposit_money(current_account,amt):
                    self.__current_account_holders.append(current_account)
                    print("Account created successfully!")
                
                else:
                    print("Account creation failed!")
            else:
                print(f"Amount should be greater than minimum balance of {current_account.minimumBalance}") 

    def withdraw_money(self):
        accountNumber = int(input("Enter account number: ")) 
        accountHolderName = input("Enter account holder name: ")
        accountType = input("Enter account type (Saving/Current): ")

        if self.isAccountExists(accountNumber, accountHolderName, accountType):
            amount = int(input("Enter amount to withdraw: "))
            if accountType.lower() == "saving":
                for account in self.__saving_account_holders:
                    if account.accountNumber == accountNumber and account.accountHolderName == accountHolderName:
                        if account.balance - amount >= account.minimumBalance:
                            account.balance -= amount
                            print(f"Withdrawn {amount} successfully. New balance is {account.balance}")
                        else:
                            print(f"Insufficient balance. Minimum balance of {account.minimumBalance} is required.")
            elif accountType.lower() == "current":
                for account in self.__current_account_holders:
                    if account.accountNumber == accountNumber and account.accountHolderName == accountHolderName:
                        if account.balance - amount >= account.minimumBalance:
                            account.balance -= amount
                            print(f"Withdrawn {amount} successfully. New balance is {account.balance}")
                        else:
                            print(f"Insufficient balance. Minimum balance of {account.minimumBalance} is required.")
        else:
            print("Account does not exist.")
    def start(self):
        
        while True:

            print("Welcome to the Bank Service")

            for key, value in self.services.items():
                print(f"{key}. {value}")

            choice = int(input("Enter your choice: "))
            
            value = self.services[choice].lower().replace(" ", "_")
            
            try:
                getattr(self,value)()

            except AttributeError as a:
                print(f"Error: {a}")
                print("Invalid choice")
            
        