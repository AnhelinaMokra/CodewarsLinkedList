"""Convert a linked list to a string"""
def stringify(node):
    """converts linked list to a string"""
    if node is None:
        return 'None'
    res = ''
    cur = node
    while cur.next is not None:
        res+= str(cur.data) + ' -> '
        cur = cur.next
    res += str(cur.data)
    res += ' -> None'
    return res
