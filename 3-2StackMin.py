# -*- coding: utf-8 -*-
"""
Created on Mon Jun 06 17:33:53 2016

@author: The Hollowed

Here we want a stack that can also produce the min value.

pop, push, and min should all be O(1)


The way to do this is to keep the min values in a stack as well.  If we push something that becomes the new min on the real stack,
the min stack gets that added too as well.  if we pop a min, same for the min stack.  If we want to see the min value, we just peek at the min stack


"""

class Stack:
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
            
    def push(self, item):
        self.items.append(item)
        return self
     
    def pop(self):
        print('pop!')
        item = self.items[-1]
        self.items = self.items[0:(len(self.items)-1)]
        return item

    def peek(self):
        if self.is_empty() == False:
            return self.items[len(self.items)-1]
        else:
            return None

    def print_stack_items(self):
        print('printing stack')
        for i in range(len(self.items)):
            print(self.items[i]),
        print("\n")        
                
    def size(self):
        return len(self.items)

        
class Stack_with_min(Stack):
    min_stack = Stack()
                
    def push(self, item):
        self.items.append(item)
        if self.min_stack.is_empty():
            self.min_stack.push(item)
        elif item < self.find_min():
            self.min_stack.push(item)
        return self
     
    def pop(self):
        print('pop!')
        item = self.items[-1]
        if item == self.min_stack.peek():
            self.min_stack.pop()
        self.items = self.items[0:(len(self.items)-1)]
        return item
        
    def find_min(self):
        if self.is_empty():
            return 0
        return self.min_stack.peek()


        
        
stack = Stack_with_min()
stack.push(4)
stack.print_stack_items()
print(stack.find_min())
stack.push(5)
stack.print_stack_items()
print(stack.find_min())
stack.push(2)
stack.print_stack_items()
print(stack.find_min())
stack.push(1)
stack.print_stack_items()
print(stack.find_min())
stack.push(10)
stack.print_stack_items()
print(stack.find_min())
stack.pop()
stack.print_stack_items()
print(stack.find_min())
stack.pop()
stack.print_stack_items()
print(stack.find_min())
stack.pop()
stack.print_stack_items()
print(stack.find_min())
stack.pop()
stack.print_stack_items()
print(stack.find_min())




