# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None :
            return head
        
        fake = ListNode()
        fake.next = head
        
        srt = fake
        curr = fake.next
        VAL = 999
        
        while curr is not None :
            
            if VAL != curr.val :
                srt.next = curr
                VAL = curr.val
                srt = curr
            
            curr = curr.next
        
        srt.next = None
        
        return fake.next
                
        