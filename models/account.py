class Account:

    accountNumber = 10000
    accountHolderName =None
    balance = 0
    phoneNumber = None
    address = None
    accountType = None
    createdDate = None
    

    def generateAccountNumber(self):
        self.accountNumber += 1
        return self.accountNumber
    
    