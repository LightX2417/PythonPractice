class Parent:
    def display(self):
        return "Parent display"


class Child(Parent):
    def display(self):
        return "Child display"


child = Child()
print(child.display()) 
