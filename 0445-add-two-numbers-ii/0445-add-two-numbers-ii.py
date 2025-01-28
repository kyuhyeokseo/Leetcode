# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        N1, N2 = [], []

        if not l1:
            return l2
        elif not l2:
            return l1
        
        c1, c2 = l1, l2
        while c1 :
            N1.append(c1.val)
            c1 = c1.next
        while c2 :
            N2.append(c2.val)
            c2 = c2.next
        
        next = None
        C = 0

        while N1 or N2 :
            if N1: n1 = N1.pop()
            else : n1 = 0

            if N2: n2 = N2.pop()
            else : n2 = 0

            now_val = n1 + n2 + C
            C = now_val // 10
            now_val %= 10

            curr = ListNode(now_val, next)
            next = curr
        
        if C == 1 :
            curr = ListNode(1, next)
        
        return curr


