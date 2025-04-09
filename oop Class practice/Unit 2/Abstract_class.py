from abc import *
class Person(ABC):
    @abstractmethod   
    def kids(self):
        print("Playing")  
    @abstractmethod         
    def happy(self):
        print("Money")
@abstractmethod
class aadmi(Person):
    def bad(self):
        print("Unhealthy")
    def kids(self):
        print("Playing")
   
        
a=aadmi()
a.bad()
a.kids()