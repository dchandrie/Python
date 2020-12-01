# parent class
#child classes will be employee
#  You need to have 3 employees with name, age and id
#function will collect the hours they worked
class employee:
    def __init__(self, name, age, id, hours):
        self.name=name
        self.age=age
        self.id=id
        self.hours = hours
    def show(self):
        print("My name is "+str(self.name)+", my age is "+ str(self.age)+ ", my id is "+str(self.id)+  ", and I worked "+str(self.hours)+" hours.")
e1 = employee("Arjun", 15, 2307, 1201)
e1.show()
e2 = employee("Shyam", 26, 2308, 1231)
e2.show()
e3 = employee("Shiva", 14, 2305, 1700)
e3.show()