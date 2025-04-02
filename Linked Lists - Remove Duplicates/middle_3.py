class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None or head.next is None:
        return head
    node =  head
    while node and node.next:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head