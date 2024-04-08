"""Can you get the loop ?"""

def loop_size(node):
    """finds a loop size"""
    slow = node
    fast = node
    while fast!=None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = node
            while fast!=slow:
                slow = slow.next
                fast = fast.next
            start = slow  
            break
    count = 1
    temp = start.next
    while temp!=start:
        count +=1
        temp = temp.next
    return count
