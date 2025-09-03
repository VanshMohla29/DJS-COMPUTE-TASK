class BankAccount:
    def __init__(self,id,name,balance):
        self.id=id
        self.name=name
        self.balance=balance
    def checkBal(self):
        print("Balance of "+self.name+" is: "+str(self.balance))
    def deposit(self,n):
        self.balance+=n
        print("Amount Credited!")
        self.checkBal()
    def withdraw(self,n):
        self.balance-=n
        print("Amount Debited!")
        self.checkBal()

ac1=BankAccount("A123","Alice",1000)
ac2=BankAccount("A234","Bob",2000)
ac1.checkBal()
ac2.checkBal()
ac1.deposit(1000)
ac2.deposit(2000)
ac1.withdraw(500)
ac2.withdraw(100)