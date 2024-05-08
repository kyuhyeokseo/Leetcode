# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None :
            return head
        
        dup = 0
        prev = ListNode(-101, head)
        dummy = prev
        curr = head
        curr_val = curr.val
        
        while curr is not None :
            
            if curr.next is not None :
                if curr.next.val != curr_val and dup == 0:
                    prev = curr
                    curr = curr.next
                    curr_val = curr.val
            
                elif curr.next.val != curr_val and dup == 1 :
                    dup = 0
                    curr = curr.next
                    prev.next = curr
                    curr_val = curr.val
                    
                else :
                    dup = 1
                    curr = curr.next
            
            else :
                if curr_val == curr.val and dup == 1:
                    prev.next = curr.next
                
                curr = curr.next
        
        return dummy.next
        