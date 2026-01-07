class bank():
    def __init__(self):
        self.balance = 0
    def deposit(self):
        amount = int(input("Enter Your Deposit Amount = "))
        self.balance += amount
        print("Amount Deposit are = ",amount)
    def withdraw(self):
        wa=int(input("What is Your Withdraw Amount = "))
        if self.balance >= wa:
            self.balance -= wa
            print("succesfull withdrawal",wa) 
        else:
            print("Insufficient Balance")
    def display(self):
        print("Net Available Balance = ",self.balance)
s=bank()
s.deposit()
s.withdraw()
s.display()