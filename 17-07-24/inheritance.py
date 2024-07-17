class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"


dog = Dog("Jo")
cat = Cat("Tom")
print(dog.speak())  
print(cat.speak())  