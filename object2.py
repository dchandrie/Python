class Dog:
    def __init__(self,name):
        self.name = name
    def add_one(self, x):
        return x+1
    def bark(self):
        print("bark")
d1 = Dog("Tim")
print(d1.name)
d1.bark()
print(d1.add_one(5))