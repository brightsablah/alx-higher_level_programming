#!/usr/bin/python3
"""New Singly List Module"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")   
        self.__data = value


    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next node must be a node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None  # Initializing the list as empty

    def sorted_insert(self, value):
        new_node = Node(value, None)

        # Case 1: If the list is empty (i.e., head is None)
        if self.__head is None:
            self.__head = new_node
        # Case 2: If the new node should be the new head (smaller than current head)
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.head = new_node

        else:
            # Traverse the list to find the correct spot for the new node
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            # Insert the new node in the correct spot
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        # Initialize an empty list to collect node data
        result = []
        current = self.__head
        
        while current is not None:
            # Append each node's data to the result list
            result.append(str(current.data))
            current = current.next_node

        # Join the result list into a string with each value on a new line
        return "\n".join(result)  # This converts the result list into a string with newline separators
