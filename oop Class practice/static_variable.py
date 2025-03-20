class Test:
    x=10        # static variable
    def __init__(self):
        self.y=20

t1=Test()
t2=Test()
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)        

Test.x=999   # changing static variable
t1.y=555    # changing a local variable

print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)  