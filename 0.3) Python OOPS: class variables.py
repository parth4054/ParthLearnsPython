
class Car:

    wheels = 4   # static or class variable, same for all objects.

    def __init__(self):
        self.millage = 10    # object specific variable
        self.company = "BMW"


c1 = Car()
c2 = Car()

c1.millage = 8

Car.wheels = 5

print(c1.company, c1.millage, c1.wheels)   # can also write Car.wheels instead of c1.wheels
print(c2.company, c2.millage, c2.wheels)

