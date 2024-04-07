"""Linked Lists - Get Nth Node"""
def get_nth(node, index):
    """gets node by index"""
    counter = 0
    while node.data is not None:
        if index==counter:
            return node
        node = node.next
        counter+=1
    return "Invalid index value should throw error."
