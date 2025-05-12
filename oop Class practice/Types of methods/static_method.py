class Hotel:
    @staticmethod
    def add (self,a):
        print(self+a)
h=Hotel
h.add(5,3)


'''
class Hotel:
    def add (self,a):
        print(self+a)
h=Hotel
h.add(5,3)          #instance method
Hotel.add(10,1)      #static method
'''     