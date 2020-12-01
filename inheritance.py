class pet:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def show(self):
        print("I am "+ str(self.name)+" and I am "+str(self.age)+" years old!")
    def speak(self):
        print("Hi!")
class cat(pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color=color

    def speak(self):
        print("Meow")
class Dog(pet):
    def speak(self):
        print("Bark")
class Fish(pet):
    pass
p=pet("Tim", 19)
p.show()
p.speak()
c=cat("Bill", 34, "blue")
c.show()
c.speak()
d=Dog("Jill", 25)
d.show()
d.speak()
f=Fish("Mean", 1)
f.show()
f.speak()