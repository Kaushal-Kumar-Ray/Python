'''class Boy:
    legs=3
    @classmethod
    def details(cls,name):
        print(f"Hi {name} you have {cls.legs} legs")
b=Boy()
b.details("Amit")
Boy.details("Aditya")       
#b.Boy("Rahul")'''

class Hotel:
    count=0
    def __init__(self):
        Hotel.count+=1
    @classmethod
    def disp(cls):
        print(cls.count)
p=Hotel()
q=Hotel()
Hotel.disp()            