class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError

    first = head
    second = head.next
    curr1 = first
    curr2 = second
    current = head.next.next
    t = True

    while current:
        if t:
            curr1.next = current
            curr1 = curr1.next
        else:
            curr2.next = current
            curr2 = curr2.next
        t = not t
        current = current.next

    curr1.next = None
    curr2.next = None

    return Context(first, second)
