class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """
    push a new value to the start of the linked list
    """
    new_val = None
    new_val = Node(data)
    new_val.next = head
    return new_val

def build_one_two_three():
    """
    build the basic linked list with values 1-3 
    """

    next_val = None
    for i in range(3, 0, -1):
        n = Node(i)
        n.next = next_val
        next_val = n
    return next_val
