from datetime import date

from models.account import Account


class Current (Account):
    def __init__(self, accountHolderName, phoneNumber, address):
        self.accountNumber = Account.generateAccountNumber(self)
        self.accountHolderName = accountHolderName
        self.phoneNumber = phoneNumber
        self.address = address
        self.accountType = "Current"
        self.createdDate = date.today()
        self.minimumBalance =1000


