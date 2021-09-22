#imports
import pytest

#define node
class Node:
    def __init__(self, payload, next = None):
        self.payload = payload
        self.next = next

class LinkedList:
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
    
    def insert_at_begining(self, payload):
        """
        Insert node at the begining of the linked list

        Parameters 
        ----------
        payload: any
            Payload to insert
        """ 
        if payload == None:
            raise "ValueError"

        if self.size == 0:
            self.__init_linked_list(payload)
            return
        
        if self.size > 0:
            node = Node(payload)
            node.next = self.head
            self.head = node
            self.size += 1

    def insert_at_end(self, payload):
        """
        Insert payload at the end of linked list
        
        Parameters
        ----------
        payload: any
            payload to insert
        """

        if payload == None:
            raise "ValueError"

        if self.size == 0:
            self.__init_linked_list(payload)
            return
        
        if self.size > 0:
            self.tail.next = Node(payload)
            self.tail = self.tail.next
            if self.size == 1:
                self.head.next = self.tail
            self.size += 1

    def display_list(self):
        """
        Display all the element in the linked list
        """
        node = self.head
        for _ in range(self.size):
            print(node.payload)
            node = node.next
        
    def find(self, payload):
        """
        Find payload in linked list, Where index starts from 0

        Return
        ------
        Index of payload if found otherwise returns -1
        """
        node = self.head
        for idx in range(self.size):
            if node.payload == payload:
                return idx
            node = node.next
        return -1
        
    def __init_linked_list(self, payload):
        self.head = Node(payload)
        self.tail = self.head
        self.size = 1

#===================Test Case 1==========================#
def test_initialization():
    
    ll = LinkedList()
    assert len(ll) == 0
    assert ll.head == None
    assert ll.tail == None

#===================Test Case 2==========================#
def test_insertion_in_begining():

    ll = LinkedList()
    ll.insert_at_begining(1)
    assert len(ll) == 1
    assert ll.head.payload == 1
    assert ll.tail.payload == 1

#===================Test Case 3==========================#
def test_multiple_insertion_in_begining():

    ll = LinkedList()
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    assert len(ll) == 2
    assert ll.head.payload == 2
    assert ll.tail.payload == 1

#===================Test Case 4==========================#
def test_insertion_in_end():

    ll = LinkedList()
    ll.insert_at_end(1)
    assert len(ll) == 1
    assert ll.head.payload == 1
    assert ll.tail.payload == 1

#===================Test Case 5==========================#
def test_multiple_insertion_in_end():

    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    assert len(ll) == 2
    assert ll.head.payload == 1
    assert ll.tail.payload == 2

#===================Test Case 6==========================#
def test_find():
    ll = LinkedList()
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.insert_at_begining(4)
    ll.insert_at_begining(5)
    assert len(ll) == 5
    assert ll.find(5) == 0
    assert ll.find(9) == -1
    