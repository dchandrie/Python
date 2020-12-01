# Need to have two child functions penguin and parrot
# Each one ask the question if it will fly
# Each one ask the question if it will swim
# Have a function outside the class if the bird can fly

class Penguin:
     def fly(self):
         print("Penguin can't fly!")

class Parrot:
    def fly(self):
        print("Parrots can fly!!!")

def fly_test(Bird):
    Bird.fly()

p =Parrot()
fly_test(p)
n = Penguin()
fly_test(n)