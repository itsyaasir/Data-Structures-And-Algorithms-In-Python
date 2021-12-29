# One end of the queue is called a front and the other end is called a rear. Items are inserted in the rear end and are removed from the front end. A queue is called a First In First Out data structure because the item that goes first comes out first.
import sys


class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class Queue:
    def __init__(self) -> None:  # Initialization of Queue
        self.rear = None
        self.front = None

    def isEmpty(self):  # Checking if the Queue is empty
        return self.front == None

    def enqueue(self, data):  # Adding data to the rear end of the queue
        newNode = Node(data)
        if self.rear == None:
            self.rear = self.front = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        # return "Node Enqueued"

     # Remove item from front node
    def dequeue(self):  # Remove data from the front end of the queue
        if self.isEmpty():
            return -1  # queue underflow
        data = self.front
        self.front = data.next

        if(self.front == None):
            self.rear = None

    # This is for showing the front value

    def peek(self):
        # Gtetting data at the front Queue
        print("Front : " + self.front.getData())
        # Getting data at the rear
        print("Rear : " + self.rear.getData())

    # Displays the Queue
    def display(self):
        if self.isEmpty():
            print("Empty Queue")
        current = self.front
        elems = []
        while current is not None:
            elems.append(current.getData())
            current = current.getNext()
            print("->".join(elems))


myQueue = Queue()


def menu():

    print('''
    Enter a number for :
    1.Enqueue 
    2.Dequeue 
    3.Display the Queue
    4.Peek
    5.Quit
    ''')
    userData = input()
    if (userData == "1"):
        myQueue.enqueue(input("Enter the value to Enqueue : "))
        print("Enqueued Successfully")
        main()
    elif(userData == "2"):
        # to check if the queue is empty
        myQueue.dequeue()
        print("Dequeued Successfully")
        main()
    elif (userData == "3"):
        if myQueue.isEmpty():
            print("Empty Queue")
            main()
        else:
            myQueue.display()
            main()
    elif(userData == "4"):
        if myQueue.isEmpty():
            print("Empty Queue")
            main()
        else:
            myQueue.peek()
            main()
    elif(userData == "q"):
        sys.exit()


def main():
    menu()


main()
