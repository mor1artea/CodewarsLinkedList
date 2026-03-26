class Node:
    """
    A simple linked list node class.
    """
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """Swaps every two adjacent nodes in a linked \
    list and returns the head of the modified list."""
    if not head or not head.next:
        return head

    a = head
    b = head.next
    new_head = b
    a.next = b.next
    b.next = a
    prev = a
    p = a.next

    while p and p.next:
        a = p
        b = p.next
        prev.next = b
        a.next = b.next
        b.next = a
        prev = a
        p = a.next

    return new_head
