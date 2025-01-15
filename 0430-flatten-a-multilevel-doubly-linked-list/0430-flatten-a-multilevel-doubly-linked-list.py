"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None :
            return None
        
        end = self.flatten_detail(head)
        return head

    def flatten_detail(self, head):
        
        curr, nxt = head, head.next

        while curr :

            if curr.child is not None :
                child_end = self.flatten_detail(curr.child)
                #print(curr.val, child_end.val)
                child_end.next = nxt
                if nxt :
                    nxt.prev = child_end
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            
            if curr.next is None :
                break
            else :
                nxt = curr.next.next
                curr = curr.next
        
        return curr



