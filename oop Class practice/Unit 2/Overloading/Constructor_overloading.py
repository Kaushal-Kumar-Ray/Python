'''
class c:
    def __init__(self,a):
        self.a=a
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a+b)
c=c(3,2)
'''
class car:
    def __init__(self,name,model,speed):
        self.name=name
        self.model=model
        self.speed=speed
    def __add__(x,y):
        print(x.speed+y.speed)
        
    def __sub__(x,y):
        print(x.speed-y.speed)
        
    def __mul__(x,y):
        print(x.speed*y.speed)
        
    def __truediv__(x,y):
        print(x.speed/y.speed)
        
c1=car("Thar",12812,80)
c2=car("Nano",24637,60)
c1+c2
c1-c2
c1*c2
c1/c2