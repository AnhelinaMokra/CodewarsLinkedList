"""Linked Lists - Alternating Split"""
from node import Node

class Context(object):
    """context class"""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """takes one list and divides up its nodes to make two smaller lists"""
    first = Node(head.data)
    second = Node(head.next.data)

    counter = 1
    cur_f = first
    cur_s = second
    head = head.next.next

    while head is not None:
        if counter%2 == 0:
            cur_s.next = Node(head.data)
            cur_s = cur_s.next
        else:
            cur_f.next = Node(head.data)
            cur_f = cur_f.next
        counter += 1
        head = head.next
    return Context(first, second)
