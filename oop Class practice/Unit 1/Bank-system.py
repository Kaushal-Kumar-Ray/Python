class Bank:
    def __init__(self,name,id,accn,balance):
        self.name=name
        self.id=id
        self.accn=accn
        self.balance=balance   
    def withdraw(self,amount):
        self.balance=self.balance-amount
    def deposite(self,amount):
        self.balance=self.balance+amount
    def disp(self):
        print("Name:",self.name, "Balance:",self.balance)

Kaushal=Bank("Kaushal",123,10000043,500)
print("-----Balance after withdraw-----")
Kaushal.withdraw(200)
Kaushal.disp()
print("-----Balance after deposite-----")
Kaushal.deposite(100000)
Kaushal.disp()

                    