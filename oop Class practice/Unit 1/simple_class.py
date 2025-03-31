'''class Human_body:
    eye=2
    leg=2
    def speak(self):
        print("Hello I am Human")
        
person=Human_body() 
print(person.eye)
print(person.leg)
person.speak()       

'''
# Uncommented and fixed Human_body class

# Fixed calculator class
class calculator:
    def __init__(self):
        self.s = 0
        self.t = 0

    def ask(self):
        self.s = int(input("Enter number first: "))
        self.t = int(input("Enter number second: "))

    def sum(self):
        self.s = self.s + self.t

    def disp(self):
        print("The sum is:", self.s)

# Using the calculator class
c = calculator()
c.ask()
c.sum()
c.disp()
print( calculator.__doc__)