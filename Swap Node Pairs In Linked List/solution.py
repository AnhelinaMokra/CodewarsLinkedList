"""Swap Node Pairs In Linked List"""
class Node:
    """node class"""
    def __init__(self, next_=None):
        self.next = next_

def swap_pairs(head):
    """swaps pairs in linked list"""
    test = Node()
    test.next = head
    prev = test

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return test.next
