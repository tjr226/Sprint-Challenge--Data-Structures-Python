# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        # self.size = 0
        # Why is our DLL a good choice to store our elements?
        ''' lets us put into and grab from top of stack in constant time '''
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        # self.size = self.storage.length

    def pop(self):
        popped_value = self.storage.remove_from_head()
        # self.size = self.storage.length
        return popped_value

    def len(self):
        return self.storage.length
