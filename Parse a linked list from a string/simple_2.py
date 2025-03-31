class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next




def linked_list_from_string(s):
    if s == "None":
        return None
    split_nodes = s.split(" -> ")[:-1]
    head = Node(int(split_nodes[0]))
    current = head
    for node in split_nodes[1:]:
        current.next = Node(int(node))
        current = current.next
    return head