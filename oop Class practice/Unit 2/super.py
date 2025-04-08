'''class p:
    def __init__(self):
        print("Parent class")
        self.b=10
class Q(p):
    pass
mp=Q()
print(mp.b)
        '''
        
class p:
    def __init__(self):
        print("Parent class")
        self.b=10
class Q(p):
    def __init__(self):
        super().__init__()
        print("child class")
mp=Q()
print(mp.b)
               
        
        
        
    