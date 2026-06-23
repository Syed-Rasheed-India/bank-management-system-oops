from models.account import Account
from datetime import date

class SavingAccount(Account):
    
    def __init__(self, accountHolderName, phoneNumber,address):
        self.accountNumber = Account.generateAccountNumber(self)
        self.accountHolderName = accountHolderName
        self.phoneNumber = phoneNumber
        self.address = address
        self.accountType ="Savings"
        self.createdDate = date.today()
        self.interestRate = 0.04
        self.minimumBalance = 500
    
    