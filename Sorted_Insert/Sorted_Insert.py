
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):

    new_node = Node(data)
    p = head
    if not head:
        return new_node

    if data < head.data:
        new_node.next = head
        return new_node
    while p:
        try:
            if p.data < data < p.next.data:
                new_node.next = p.next
                p.next = new_node
                break
        except AttributeError:
            p.next = new_node
            break

        p = p.next

    return head
