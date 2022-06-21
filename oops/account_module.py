class Account:
    __balance = 0

    def deposite(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance > 0:
            self.__balance = self.__balance - amount

    def getBalance(self):
        return self.__balance
