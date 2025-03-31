class Dashrath:
    def aashirwad(self):
        print("sada suhagan raho")
class Ram():
    #def blessing(self):
    def aashirwad(self):
        print("Maryada hai")
        
class Lavkush(Dashrath,Ram):
    def fight(self):
        print("Justice")
s=Lavkush()
s.fight()        
#s.blessing()
s.aashirwad()