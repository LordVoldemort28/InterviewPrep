import pytest

class Node:
    def __init__(self, payload, next=None, previous=None):
        self.payload = payload
        self.next = next
        self.previous = previous

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        """
        Get the size of list

        Return
        ------
        Length of the linked list
        """
        return self.size

    def insert_at_begining(self, payload: str):
        """
        Insert node at begining
        """
        if self.size == 0:
    