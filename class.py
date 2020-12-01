# class PERSON:
#     age =10
#     name=deepa
#     color=green
#     "This is a person class"
#     def greet (self):
#         print("hello")
# print(PERSON.greet)
# print(PERSON.age)
# print(PERSON.name)
# print(PERSON._doc_)
class dog:
    def add_one(self, x):
        return x + 1
    def bark(self):
        print("bark, bark")
d = dog()
print(d)
d2 = dog()
print(d2)
d.bark()
print(d.add_one(5))
print(type(d))
print(type(d2))