class Node():
    """"
    Node class for a linked list
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node: Node):
    """
    Convert a linked list to a string representation.

    >>> stringify(Node(1, Node(2, Node(3))))
    "1 -> 2 -> 3 -> None"

    >>> stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))
    "0 -> 1 -> 4 -> 9 -> 16 -> None"
    """

    if not node:
        return 'None'

    curr = node
    result = []

    while node:
        result.append(str(curr.data))
        if curr.next:
            curr = curr.next
        else:
            result.append("None")
            break

    return ' -> '.join(result)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
