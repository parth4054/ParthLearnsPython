# Video Link: https://www.youtube.com/watch?v=lVfGQOzzRCM&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=57
# 3 kinds of methods - Instance Methods, Class Methods, Static Methods

class Student:

    school = "Ahlcon Public School"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):   # Instance Method - to access instance variables
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def school_name(cls):   # class method - to access class/static variables
        return cls.school

    @staticmethod
    def info():
        print("I am a static method")  # static method - nothing to do with class/static variables or instance variables


s1 = Student(5, 10, 29)
s2 = Student(23, 34, 12)

print(s1.average())
print(s2.average())

print(Student.school_name())

