"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    current = head
    temp = None
    if(head.next == None):
        return head
    else:
        while(current != None):
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        return temp.prev

