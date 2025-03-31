def stringify(node):
    if node is None:
        return "None"
    result = ""
    while node:
        result += str(node.data) + " -> "
        node = node.next      
    return result + "None"