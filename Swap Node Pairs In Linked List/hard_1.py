from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    new_head = head.next
    head.next = swap_pairs(new_head.next)
    new_head.next = head
    return new_head
