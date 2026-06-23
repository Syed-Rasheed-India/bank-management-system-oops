
from models.saving_account import SavingAccount
class BankService:
    
    services ={1: "Create Saving Account", 2: "Create Current Account", 3: "Withdraw Money", 4: "Deposit Money", 5: "Transaction History", 6: "Exit"}
    __saving_account_holders = []
    
    def getDetils(self):

        accountHolderName = input("Enter account holder name: ")
        phoneNumber = input("Enter phone number: ")
        address = input("Enter address: ")
        return accountHolderName, phoneNumber, address
    
    def create_saving_account(self):
        
        accountHolderName, phoneNumber, address = self.getDetils()
        
        saving_account = SavingAccount(accountHolderName, phoneNumber, address)
        
        if saving_account.balance < saving_account.minimumBalance:
            print(f"Minimum balance of {saving_account.minimumBalance} is required. so Please deposit money to create account")
            #deposit money to create account
            #if deposited then append to saving_account_holders list 

    
    def start(self):

        print("Welcome to the Bank Service")

        for key, value in self.services.items():
            print(f"{key}. {value}")

        choice = int(input("Enter your choice: "))
        
        value = self.services[choice].lower().replace(" ", "_")
        
        try:
            getattr(self,value)()

        except AttributeError:

            print("Invalid choice")
            
        