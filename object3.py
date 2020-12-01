class Dog:
    def __init__(self,name,age, gender):
        self.name=name 
        self.age=age
        self.gender = gender
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
d1 = Dog("Tim",15, "male")
print(d1.get_name(),d1.get_age(), d1.get_gender())


