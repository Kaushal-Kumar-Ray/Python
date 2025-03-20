class atrh:
    def __init__(self,x,y):
        self.t=x
        self.s=y
    def change(self):
        self.s=20
    def solve(self):
        self.t=self.t+self.s
        print(self.t)
a=atrh(10,30)
a.change()
a.solve()        