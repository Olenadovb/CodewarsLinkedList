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
    first_head = first
    second_head = second
    while first and second and second.next:
        first.next = second.next
        first = first.next
        second.next = first.next
        second = second.next
    first.next = None
    return Context(first_head, second_head)