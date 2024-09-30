# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        stkA = []
        stkB = []
        
        currA = headA
        currB = headB
        
        while currA is not None or currB is not None :
                
            if currA is not None :
                stkA.append(currA)
                currA = currA.next
            
            if currB is not None :
                stkB.append(currB)
                currB = currB.next
        
        prev = None
        while stkA and stkB:
            tmpA = stkA.pop()
            tmpB = stkB.pop()
            
            if tmpA != tmpB :
                return prev
            
            if tmpA == tmpB :
                prev = tmpA
            
        return prev
        
        
        
        
        