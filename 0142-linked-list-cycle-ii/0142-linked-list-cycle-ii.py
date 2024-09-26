# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None :
            return None
        
        slow = fast = head
        cnt = 0
        
        while fast and fast.next :
            
            fast = fast.next.next
            slow = slow.next
            cnt += 1
            
            if fast == slow :
                break
        
        if fast is None :
            return None
        elif fast.next is None :
            return None
        
        while slow != head :
            slow = slow.next
            head = head.next
        
        return slow
            
        
        
        
        
        
        