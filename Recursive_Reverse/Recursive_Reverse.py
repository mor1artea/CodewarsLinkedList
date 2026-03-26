class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head):
    """
    Recursive Reverse
    """

    if not head:
        return None
    if not head.next:
        return head

    new_head = reverse(head.next)

    head.next.next = head
    head.next = None

    return new_head
