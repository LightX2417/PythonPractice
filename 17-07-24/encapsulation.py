class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

person = Person("Alice", 30)
print(person.get_name())  
person.set_name("Bob")
print(person.get_name()) 
