import sys


class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    # def getNext(self):
    #     return self.next

    # def setNext(self, value):
    #     self.next = value


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def isEmpty(self):
        """ Check if the list is empty """
        return self.head is None

    def add(self, userData):
        """Add the userData to the list """
        newNode = Node(userData)
        newNode.next = self.head
        self.head = newNode

    def size(self):
        """ Return the length of the list """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, userData):
        """ Search for userDatas in list. If found return True. If not found , return False """
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is userData:
                found = True
            else:
                current = current.next
        return found

    def remove(self, userData):
        """ Remove userData from list, If userData is not found in list , raise ValueError"""
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() is userData:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            if previous is None:
                self.head = current.next
            else:
                # previous.setNext(current.next)
                previous.next = current.next
        else:
            print("Value doesn't Exist ")
            raise ValueError

    def display(self):
        """Prints the list"""
        current = self.head

        elems = []
        while current is not None:
            elems.append(current.getData())
            current = current.next
            print("->".join(elems))

    def total(self):
        """Prints the total of the Linked List"""
        current = self.head
        elems = []
        while current is not None:
            val = 0
            elems.append(current.getData())
            for elem in elems:
                val = int(int(elem) + val)
            current = current.next
        print(val)


myList = LinkedList()


def main():
    menu()


def menu():
    """ List all the menu of the program """

    choice = int(input("""
    --------------------MENU-----------------------
    Choose the following Options:
    1.Add a number
    2.Remove a number
    3.Total of the number
    4.Search a number
    5.Display the Linked List
    6.Quit
    Please Enter your choice :
    """))
    if choice == 1:
        userData = input(
            "Enter the number you want to add / Enter q to return to Main Menu: ")
        if userData == "q":
            main()
        else:
            myList.add(userData)
            myList.display()
            print("Number added succesfully")
            main()

    if choice == 2:
        userData = input(
            "Enter the number you want to remove/ Enter q to return to Main Menu : ")
        if userData == "q":
            main()
        else:
            myList.remove(userData)
            myList.display()
            main()
        print("Number removed successfully")
    if choice == 3:
        myList.total()
        main()
    if choice == 4:
        userData = input(
            "Enter the number you want to search : ")
        myList.search(userData)
        main()

    if choice == 5:
        myList.display()
        main()
    if choice == 6:
        sys.exit()


main()

# Array is a sequential collection in memory of fixed size of objects each of same type
