# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None :
            return head
        
        elif head.next is None :
            return head
        
        else :
            
            prev = ListNode()
            start = prev
            
            x = head
            y = x.next
            prev.next = x
            
            while x is not None and y is not None :
                
                tmp = ListNode()
                tmp.next = y.next
                y.next = x
                prev.next = y
                x.next = tmp.next
                
                prev = x
                x = prev.next
                
                if x is None :
                    return start.next
                
                y = x.next
                
            return start.next
                
                
            
            
            
        
        
        
        
        
        