class myBudget:
    """
    This is Sophie's Budgeting App
    """
    pass
    def __init__(self, category, balance):
        self.category = category
        self.balance = 0


    def deposit(self,depositAmount):
        try:
            if depositAmount <= 0:
                return "You have entered an invalid amount"
            else:
                self.balance += depositAmount
                print("You have deposited {} into your {} budget".format(depositAmount, self.category))
                print("Your {} is now {}".format(self.category, self.balance))
        except:
            return ("Invalid Input")

    def withdrawal(self,withdrawAmount):
        if withdrawAmount <= self.balance:
            self.balance -= withdrawAmount
            print("You have just withdrawn {} from your {} budget".format(withdrawAmount,self.category))
            return self.categoryBalance()
        else:
            return "Your balance is insufficient"

    def transfer(self,transferAmount):
        print("You have just transfered {} from your {} budget".format(transferAmount, self.category))
        return transferAmount

    def categoryBalance(self):
        return "The current balance left in the {} budget is {}".format(self.category, self.balance)


clothing = myBudget('clothing', 10000)
food = myBudget('food',5000)
entertainment = myBudget('entertainment',5000)

print(clothing.deposit(50000))
print(clothing.withdrawal(20000))
print(entertainment.deposit(50000))
print(clothing.transfer(5000))
print(entertainment.withdrawal(5000))
print(entertainment.categoryBalance())
print(clothing.transfer(5000))


print(type(myBudget))
