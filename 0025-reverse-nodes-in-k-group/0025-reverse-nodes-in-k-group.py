# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None :
            return None
        
        L = self.get_length(head)
        
        return self.reverse_(head, k, L)
        
        
    def get_length(self, start) :
        l = 0
        while start is not None :
            start = start.next
            l += 1
        return l
        
        
    def reverse_(self, head, k, L) :
        
        if k > L :
            return head
        
        prev = None
        temp = None
        curr = head
        cnt  = 0
        
        while curr is not None and cnt < k :
            temp      = curr.next
            curr.next = prev
            prev      = curr
            cnt      += 1
        
            curr      = temp
    
        if temp is not None :
            head.next = self.reverse_(temp, k, L-k)
            
        
        return prev
        
        
        
        