class book:
    def __init__(self,bname,price):
        self.name=bname
        self.cost=price
    def disp(self):
        print(self.name,self.cost)
    def __add__(c,p):
        return (c.cost+ p.cost)
b1=book("hello",199)
b2=book("states",299)
b1.disp()
c=b1+b2
print(c)    
        