"""Parse a linked list from a string"""
from node import Node
def linked_list_from_string(s):
    """parses a linked list from a string"""
    if s == 'None':
        return None
    data = [int(i) for i in s.strip().split(' -> ')[:-1:]]
    next_ = None
    for i, el in enumerate(data[::-1]):
        cur = Node(el, next_)
        next_ = cur
        if i==len(data)- 1:
            head = cur
    return head
