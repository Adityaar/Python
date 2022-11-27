"""Program to demonstrate a LinkedList or Unordered List. """


class Node:
    """ Class that defines a Node object and operations that can be
        performed on a node of a list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """ Get the value stored in current Node."""
        return self.data

    def get_next(self):
        """ Get the reference pointing to next node in the list. """
        return self.next

    def set_data(self, new_value):
        """ Set the value of the current node to new value."""
        self.data = new_value

    def set_next(self, next_node):
        """ Update the next pointer to a new node. """
        self.next = next_node

    def has_next(self):
        """ Check if the pointer in current node has reached the END"""
        return self.next is not None


class LinkedList:
    """ ADT pointing to a head of the list. """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def add(self, item):
        """ Add a new node to the FRONT of the List. """
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """ Get the size of the list. Time complexity: O(n). """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def print_list(self):
        """ Print the list of the items. """
        current = self.head
        while current is not None:
            print(str(current.get_data()))
            current = current.get_next()

    def search(self, item):
        """ Given an item, search and return True or False """
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
                break
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        """Search and Remove an item from the list. """
        current = self.head
        prev = current
        found = False
        # Check if list is empty:
        if self.is_empty():
            return False
        # If not empty and Head of the list is matching!
        if current.get_data() == item:
            found = True
            self.head = current.get_next()
            del current

        # To check nodes other than Head of the list
        while not found:
            if current.get_data() == item:
                found = True
                prev.set_next(current.get_next())
                del current
            else:
                prev = current
                current = current.get_next()
                # If the item was not found and current reached END.
                if current is None:
                    print("Item: " + str(item) + " not found")
                    break


mylist = LinkedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.add(27)
mylist.add(25)
mylist.add(23)
mylist.add(21)

print("\nBefore deletion:")

mylist.print_list()
mylist.remove(21)
print("\nAfter deletion:")
mylist.print_list()
mylist.remove(21)
print("\nAfter deletion:")
mylist.print_list()
