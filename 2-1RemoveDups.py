# -*- coding: utf-8 -*-
"""
Created on Sun May 08 14:08:26 2016

@author: John Fuini

Remove duplicates from an unsorted singly linked list
"""

class Node(object):
    value = 0
    next = None

    def __init__(self, d):
        self.value = d

    def set_next(self, node):
        self.next = node
        
    def get_value(self, node):
        return self.data
        
    def get_next(self, node):
        return self.next

             
class linked_list(object):
    head = None

    
    def __init__(self, h):
        self.head = h
        
    def add_to_head(self, node):
        temp_node = self.head
        self.head = node
        self.head.next = temp_node

    def add_from_list(self, temp_list):
        for i in temp_list:
            self.add_to_head(Node(i))
        
    def print_list(self):
        print("Printing Linked List")
        current_node = self.head    
        while current_node != None:
            print(current_node.value),
            current_node = current_node.next
        print('\n')
            
    def del_node(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return value
        current_node = self.head
        previous_node = self.head
        while current_node != None:
            if current_node.value == value:
                previous_node.next = current_node.next
                return current_node.value                
            previous_node = current_node    
            current_node = current_node.next
        print('Node not found!')
        
    def size(self):
        current_node = self.head
        temp_size = 0
        while current_node != None:
            temp_size = temp_size + 1
            current_node = current_node.next
        return temp_size
            

def remove_dups(linked_list):  #(naive inefficient implementation)
    node = linked_list.head
    while node != None:
        count = 0
        test_node = linked_list.head
        while test_node != None:
            if test_node.value == node.value:
                count = count + 1
            test_node = test_node.next
            if count > 1:
                linked_list.del_node(node.value)
                break
        node = node.next   
        
    return linked_list

entry_list = [4,1,3,2,19,148,2,3]
print(entry_list[3])

a = Node(5) 
A = linked_list(a)
A.add_from_list(entry_list)
A.print_list()
print("Removing Duplicates")
B = remove_dups(A)
B.print_list()

