
class Persons:

    def __init__(self):
        self.name = "Parth"
        self.age = 26

    def update(self):
        self.age = 30

    def compare_age(self, person2):
        if self.age == person2.age:
            return True
        else:
            return False


p1 = Persons()
p2 = Persons()

p1.name = "Annu"
p1.update()

if p1.compare_age(p2):
    print("Equal Age")
else:
    print("different age")

print(p1.name)
print(p1.age)

print(p2.name)
print(p2.age)

