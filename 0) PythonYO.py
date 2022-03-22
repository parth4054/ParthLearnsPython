
# Basics ----------------------------------------

print("Hello, Parth")

name = "Parth"
age = 26
weight = 75.2
is_cool = True

print(name)
print(age)


# User Input ----------------------------------------
# Note: User input is always a string

name = input("What is your name?")
print("Hello " + name + " hope you are doing good!")

old_age = input("enter your old age: ")
new_age = int(old_age) + 2
print("New age is " + str(new_age))  # converted age to string to concatenate with string "New age is"

first = input("Enter first number: ")
second = input("Enter second number: ")
sum1 = first + second  # Will concatenate the 2 strings
sum2 = int(first) + int(second)
print(sum1)
print("The sum is: " + str(sum2))


# Strings ----------------------------------------

name = "Parth Anand"
print(name.upper())  # The upper() function doesn't alter the original string. It returns the altered string.
print(name)  # will output Parth Anand not PARTH ANAND
print(name.lower())

print(name.find("r"))  # returns the index, if letter not present, returns -1
print(name.find("x"))  # returns -1
print(name.find("Anand"))  # returns 6

print(name.replace("Parth Anand", "The AR Guy"))  # Won't change the original string
print(name.replace("Anand", "AR Guy"))
print(name.replace("n", "m"))


# The "in" keyword ----------------------------------------

name = "Parth Anand"
print("A" in name)  # returns a bool


# Operators ----------------------------------------
# add, sub, multiply is same as maths

print(5 / 2)
print(5 // 2)  # removes the decimal
print(5 % 2)  # modulo operator, returns remainder

print(5 ** 2)  # 5 raised to the power 2

i = 5
i += 2  # means i = i + 2

# other operators <  >  ==  !=  or  and  not

print(2 > 3 or 2 > 1)
print(2 > 3 and 2 > 1)
print(not 2 > 3)


# Conditional Statements ----------------------------------------

age = 19

if age >= 18:
    print("You're an adult")
    print("You can vote!")
elif age < 18 and age > 3:
    print("You are in school")
else:
    print("You are a child")


# Range ----------------------------------------

numbers = range(5)  # returns a sequence of first 5 numbers or first n numbers. 5 not included.
print(numbers)


# Loop ----------------------------------------

i = 1
while i <= 10:
    print(i * "•")
    i += 1


for item in range(5):
    print(item)


# List ----------------------------------------
# Lists are ordered
# Lists are mutable
# Lists can be nested i.e we can also have a list inside a list
# lists are dynamic

marks = [95, 99, 97, 90]
print(marks)
print(marks[1])
print(marks[-1])
print(marks[0:2])  # only 0 and 1 index will be included
print(marks[1:4])

for score in marks:
    print(score)

marks.append(93)  # to add something at the last
marks.insert(0, 88)  # to add at a particular index

print(marks)
print(99 in marks)  # returns true or false
print(len(marks))  # length of list

i = 0
while i < len(marks):
    print(marks[i])
    i += 1

marks.clear()  # empties the list
print(marks)


# Nested List
nlist = [1, 2, ["p", "w"]]
print(nlist)


# Break & Continue statements ----------------------------------------

students = ["ram", "shyam", "kishan", "radha", "radhika"]

# Ques: print until radha, radha not included.
for student in students:
    if student == "radha":
        break
    print(student)


print("")


# Ques: print all except kishan
for student in students:
    if student == "kishan":
        continue              # continue statement transfers the control back to loop immediately.
    print(student)


# Tuples ----------------------------------------
# tuples are immutable or non changeable. lists are mutable
# ordered just like list
# tuples can be nested with other tuples as well
# tuples are faster than list

marks = (95, 96, 92, 92, 92)

print(marks.count(92))
print(marks.index(92))  # returns the index of first occurrence of 92


# Sets ----------------------------------------
# For storing unique elements, no duplicates
# Mutable
# doesn't have indices so can't access elements using index
# unordered
# Can contain only immutable elements

marks = {95, 76, 29, 98, 98}
print(marks)  # 98 will be printed once because no duplicates

for score in marks:
    print(score)


print("")


# Dictionaries ----------------------------------------
# Unordered
# can't have duplicate keys & mutable keys
# Are mutable
# Can be nested, i.e we can have another dictionary as one of the values.

marks = {"eng": 86, "maths": 95}

print(marks["eng"])
marks["phy"] = 86
print(marks)
marks["eng"] = 99
print(marks)


# Functions ----------------------------------------

# from math import *      # imports all functions
from math import sqrt     # imports a single function

print(sqrt(16))


# User Defined Functions ----------------------------------------

# def func_name (parameters):
#    do something

def add_two_numbers (num1, num2):
    print("sum is: " + str(num1 + num2))


add_two_numbers(2, 4)


def add_numbers (num1, num2=2):
    print("sum is: " + str(num1 + num2))


add_numbers(1)



