class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    """
    Get the node at the given index.
    """

    result = []
    curr = node

    while node:
        result.append(str(curr.data))
        if curr.next:
            curr = curr.next
        else:
            result.append("None")
            break

    if len(result)-1 <= index or index < 0 or not node:
        raise IndexError

    p = node
    while index != 0:
        p = p.next
        index -= 1

    return p
