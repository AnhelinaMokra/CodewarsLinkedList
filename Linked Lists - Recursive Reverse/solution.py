"""Linked Lists - Recursive Reverse"""
class Node(object):
    """node class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """reverses linked list"""
    def recursive(prev, cur):
        if cur is None:
            return prev
        next_node = cur.next
        cur.next = prev
        return recursive(cur, next_node)

    new_head = recursive(None, head)
    return new_head
