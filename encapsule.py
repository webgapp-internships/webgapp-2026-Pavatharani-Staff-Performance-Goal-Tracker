class bank_account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
    def getbalance(self):
        return self.__balance
    def setbalance(self,amount):
        if amount >= 0:
            self.__balance = amount
s1 = bank_account("tharani",5000)
print(s1.getbalance())
s1.setbalance(3000)
print(s1.getbalance())
