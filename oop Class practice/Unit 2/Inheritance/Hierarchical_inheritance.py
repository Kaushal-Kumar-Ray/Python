# Parent class
class Animal:
    def character(self):
        return "This is a pet"

# Child class 1
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# Child class 2
class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

# Child class 3
class Cow(Animal):
    def speak(self):
        return "Moo! Moo!"

# Creating objects
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the speak() and character() methods from different child classes
print("Dog:", dog.speak(), dog.character())   # Output: Woof! Woof! This is a pet
print("Cat:", cat.speak(), cat.character())   # Output: Meow! Meow! This is a pet
print("Cow:", cow.speak(), cow.character())   # Output: Moo! Moo! This is a pet