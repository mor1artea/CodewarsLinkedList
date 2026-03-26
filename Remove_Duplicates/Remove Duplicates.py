class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Remember to return the head of the list.
    p = head
    dup = None
    while p:
        if not p.next:
            break
        if p.data == p.next.data:
            dup = p.data
            d_node = p
            while p and p.data == dup:
                p = p.next
            d_node.next = p
        else:
            p = p.next
    return head
