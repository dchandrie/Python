class immigrant:
    def __init__(self, name, nationality, origin):
        self.name = name
        self.nationality = nationality
        self.origin = origin
    def get_name(self):
        return self.name
    def get_nationality(self):
        return self.nationality
    def get_origin(self):
        return self.origin
    
d1=immigrant(input("name: "), input("nationality: "), input("origin: "))
print(d1.get_name(), d1.get_nationality(), d1.get_origin())