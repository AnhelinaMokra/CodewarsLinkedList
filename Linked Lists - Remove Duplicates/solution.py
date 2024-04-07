"""Linked Lists - Remove Duplicates"""

def remove_duplicates(head):
    """removes duplicates from linked list"""
    if head is None or head.next is None:
        return head
    data = {head.data}
    cur = head
    while cur.next is not None:
        if cur.next.data not in data:
            data.add(cur.next.data)
            cur = cur.next
        else:
            cur.next = cur.next.next
    return head
