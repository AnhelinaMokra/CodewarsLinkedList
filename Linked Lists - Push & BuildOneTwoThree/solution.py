"""Linked Lists - Push & BuildOneTwoThree"""
class Node:
    """node class"""
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """adds node before another node"""
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    """creates linked list with 3 nodes"""
    head = None
    for i in range(3, 0, -1):
        head = push(head, i)
    return head
