class fiction:
    def __init__(self, name, availability):
        self.name=name
        self.availability=availability
    def show(self):
        print("Book Titled "+ str(self.name)+" is "+str(self.availability))
    def nature(self):
        print("Reading is good! You should try!!!")

class classic(fiction):
    def nature(self):
        print("Old")
class Mystery(fiction):
    def nature(self):
        print("Thrilling")
class romance(fiction):
    pass
p=fiction("The handmade tale", "Available")
p.show()
c=classic("Alice in Wonderland", "Not Available")
c.show()
c.nature()
d=Mystery("The Girl with a Dragon Tatto", "Not Available")
d.show()
d.nature()
f=romance("Brunch at the bittersweet cafe", "Available")
f.show()
f.nature()