""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    node = head
    new_node = Node(data)
    if head is None or data < head.data:
        new_node.next = head
        return new_node
    while node.next and node.next.data < data:
        node = node.next
    new_node.next = node.next
    node.next = new_node
    return head