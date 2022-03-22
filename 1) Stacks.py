# LIFO OR FILO

# OPERATIONS IN STACK -
#  Push
#  Pop
#  Peek or Top
#  isEmpty


# IMPLEMENTATION OF STACK USING LIST

stack = []


def push():
    element = input("Enter the element")
    stack.append(element)
    print(stack)


def pop_element():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Removed element " + stack.pop())
        print(stack)


def peek():
    if not stack:
        print("No element in the stack!")
    else:
        print("Top element is " + stack[-1])


while True:
    print("Select the operation you would like to perform: 1) Push  2) Pop  3) Peek  4) Quit")
    choice = int(input())

    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        peek()
    elif choice == 4:
        break
    else:
        print("Enter correct operation!")






