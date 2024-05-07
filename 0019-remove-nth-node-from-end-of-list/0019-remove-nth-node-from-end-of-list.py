# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head is None :
            return None
        
        L = self.get_Length(head)
        
        prev = None
        curr = head
        cnt = 0
        while (cnt < L-n) :
            cnt += 1
            prev = curr
            curr = curr.next
        
        if prev is None :
            head = curr.next
            return head
        
        prev.next = curr.next
        return head
        
        
    def get_Length(self, head) :
        l = 0
        while head is not None :
            l+=1
            head = head.next
        return l    
        
        