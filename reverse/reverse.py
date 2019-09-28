class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def print(self):
    node = self.head
    print(node.value)
    
    while node.next_node:
      node = node.next_node
      print(node.value)

    return

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    if self.head is None:
      return

    if self.head.next_node == None:
      return
    
    prev_node = self.head
    current_node = self.head.next_node
    next_node = current_node.next_node
    prev_node.next_node = None
    
    while current_node:
      # reverse next_node so it's pointing backwards
      current_node.next_node = prev_node
      # set head as current node
      self.head = current_node

      # this is needed for lists of length 2
      if next_node == None:
        break

      # reset vars for next loop
      # move prev_node up one
      prev_node = self.head
      # set current_node as the saved next_node
      current_node = next_node
      # these next two statements are both needed
      # move the next node, assuming there is one
      if current_node.next_node:
        next_node = current_node.next_node

      # if there is no next node, break
      if current_node == next_node:
        break

    # do the final pointer switches - needed because it's not done the final time through the loop
    current_node.next_node = prev_node
    self.head = current_node

    return

test_list = LinkedList()

test_list.add_to_head(1)
test_list.add_to_head(2)
test_list.add_to_head(3)
test_list.add_to_head(4)
test_list.add_to_head(5)

test_list.print()

test_list.reverse_list()
print("list is reversed")
test_list.print()