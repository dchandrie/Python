# parent class "Bird"
# child class "penguin"
# print "Bird/Penguin is ready!"
# both Bird and penguin should have function with a question "Why is this?" and answer should be bird/penguin.
# if it is a bird say "swim faster"
# for penguin, say run faster
class Bird:
    def __init__(self, name):
        self.name=name
    def show(self):
        print("Bird is ready!")
    def identifier(self):
        print("Who is this? "+str(self.name))
    def command(self):
        print("Swim Faster!!!!")

class Penguin(Bird):
    def show(self):
        print("Penguin is ready!")
    def identifier(self):
        print("Who is this? " +str(self.name))
    def command(self):
        print("Walk Faster!!!")
b = Bird("Crow")
b.show()
b.identifier()
b.command()

p = Penguin("Penguin")
p.show()
p.identifier()
p.command()

    
    
    

