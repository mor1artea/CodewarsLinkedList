class Node():
    """"
    Node class for a linked list
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    """
    linked list from string

    """
    if list_repr == "None":
        return None

    list_repr = list(reversed(list_repr.split(' -> ')))

    next_val = None
    for i in range(1, len(list_repr)):
        next_val = Node(int(list_repr[i]), next_val)

    return next_val

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
