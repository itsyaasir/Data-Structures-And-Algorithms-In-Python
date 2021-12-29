import sys


class Stack(object):
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    # for printing the stack contents
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    # for pushing an element on to the stack
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Stack Overflow')
        else:
            self.stack.append(data)

    # for popping the uppermost element
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

    # to check if stack is empty
    def isEmpty(self):
        return self.stack == []

    # for checking the size of stack
    def size(self):
        return len(self.stack)

    # To display the stack
    def display(self):
        print(self.stack)


myStack = Stack()


def menu():

    print("Enter a number for the following functionalites " +
          "1 for Push and 2 for Pop and 3 to display the Stack and q to quit")
    choice = input()
    if (choice == "1"):
        myStack.push(int(input("Enter the value to push : ")))
        myStack.display()
        main()
    elif(choice == "2"):
        # to check if the queue is empty
        if(len(myStack.stack) == 0):
            print("Queue is empty")
            main()
        else:
            myStack.pop()
            print("Popped Successfully")
            myStack.display()
            main()

    elif(choice == "3"):
        if(len(myStack.stack) == 0):
            print("The Stack is Empty")
        else:
            myStack.display()
        main()

    elif(choice == "q"):
        sys.exit()


def main():
    menu()


main()
