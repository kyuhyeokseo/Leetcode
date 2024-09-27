# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def getLength(head):
            cnt = 0
            while head :
                head = head.next
                cnt += 1
            return cnt
        
        L = getLength(head)
        
        if L == 0 :
            return head
        elif L == 1 :
            return head
        
        N = (L-1)//2
        
        tmp1 = head
        tmp2 = tmp1.next
        
        for _ in range(N):
            
            prev = tmp1
            curr = tmp1.next
            while curr.next :
                prev = prev.next
                curr = curr.next
            #print(tmp1.val, tmp2.val, prev.val, curr.val)
            curr.next = tmp2
            tmp1.next = curr
            prev.next = None
            
            tmp1 = tmp2
            tmp2 = tmp1.next
            
            
            #p = head
            #print('-------------')
            #while p :
            #    print(p.val)
            #    p = p.next
            #print('-------------')
        
        
        
        
        
        
        