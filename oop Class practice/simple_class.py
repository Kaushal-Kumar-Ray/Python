class Human_body:
    eye=2
    leg=2
    def speak(self):
        print("Hello I am Human")
        
person=Human_body() 
print(person.eye)
print(person.leg)
person.speak()       


class calculator:
    s=0
    t=0
    def ask(self):
        s=int(input("Enter number first"))
        t=int(input("Enter number second"))
    def sum(self):
        s=s+t
    def disp(self):
        print(s)  
c=calculator()
c.ask()
c.sum()
c.disp()              