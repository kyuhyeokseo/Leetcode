# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None :
            return None
        
        L = self.get_Length(head)
        k = k % L
        if k == 0 :
            return head
        
        cnt = 0
        new_head = head
        new_last = head
        last = head
        while cnt < L-1 :
            cnt += 1
            last = last.next
            if cnt == L-k-1 :
                new_last = last
            if cnt == L-k :
                new_head = last
            
        last.next = head
        new_last.next = None
        
        return new_head
        
    def get_Length(self, head) :
        l = 0
        while head is not None :
            head = head.next
            l+=1
        return l
        
        
        
        