class car:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    def __str__(self):
        print (self.name)
        print (self.speed)
c1=car("Thar",100)
c2=car("BMW",150)
print(c1)
print(c2)