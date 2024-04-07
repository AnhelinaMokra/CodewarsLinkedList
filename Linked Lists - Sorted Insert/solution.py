"""Linked Lists - Sorted Insert"""
from node import Node

def sorted_insert(head, data):
    """inserts data in accurate place in linked list"""
    if head is None:
        return Node(data)
    if head.data> data:
        return Node(data, head)
    cur = head
    while cur.next is not None and cur.next.data < data:
        cur = cur.next
    cur.next = Node(data, cur.next)
    return head
