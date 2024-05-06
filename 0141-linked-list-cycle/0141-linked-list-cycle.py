# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        target = head
        while (True) :
            if target is None :
                return False
            if target.val is None :
                return True
            target.val = None
            target = target.next

            
        
        
        
        
        
        
        
        
        