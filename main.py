class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello! My name is {self.name} and I am {self.age}")


p = Person('Max', 27)
p.say_hello()
