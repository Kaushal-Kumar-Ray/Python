class car:
    def __init__(self):
        self.__fuel=10
    def fill_fuel(self):
        self.__fuel=10
c=car()
c.fuel=20
print(c.fuel)