class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def loop_size(node):
    fast = node
    slow = node
    count = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = slow.next
    fast = fast.next.next
    count += 1
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
        count += 1
    return count
