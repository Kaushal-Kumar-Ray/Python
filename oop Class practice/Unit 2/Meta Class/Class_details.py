class ab:
    def __init__(self):
        self.a=11
        self.b=13
    def hello(self):
        pass
a=ab()
a.hello()
print(a.__dict__)
print(ab.__dict__)