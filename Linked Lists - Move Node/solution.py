"""Linked Lists - Move Node"""
from node import Node

class Context(object):
    """saves data"""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """moves first node from source to dest"""
    dest = Node(source.data, dest)
    source = source.next
    return Context(source, dest)
