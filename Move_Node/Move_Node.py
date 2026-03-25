class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """Move the first node from source list to dest list."""
    if not source:
        raise ValueError
    move = source
    source = source.next
    move.next = dest
    return Context(source, move)
