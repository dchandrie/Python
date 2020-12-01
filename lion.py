
class lion:
    def __init__(self, where, kind, color):
        self.where=input("where is the lion:")
        self.kind=input("what kind is the lion:")
        self.color=input("What colors is the lion:")
    def get_where(self):
        return self.where
    def get_kind(self):
        return self.kind
    def get_color(self):
        return self.color
d1 = lion("where", "kind", "color")
print(d1.get_where(), d1.get_kind(), d1.get_color())