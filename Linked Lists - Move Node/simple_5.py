class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError
    node = source.data
    new_dest = Node(node)
    new_dest.next = dest
    new_source = source.next
    return Context(new_source, new_dest)