# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head is None :
            return True
        elif head.next is None :
            return True
        
        rec = []
        curr = head
        while curr is not None :
            rec.append(curr.val)
            curr = curr.next
        
        return rec == rec[::-1]
        
        
        
        