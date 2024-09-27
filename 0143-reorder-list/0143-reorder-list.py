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
        if head is None :
            return head
        
        stack, queue = [], []
        
        slow = fast = head
        
        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
            
        s_srt = slow.next
        q_srt = head
        
        while q_srt != s_srt :
            queue.append(q_srt)
            q_srt = q_srt.next
        
        while s_srt :
            stack.append(s_srt)
            s_srt = s_srt.next
        
        #print(queue)
        #print(stack)
        
        out = ListNode()    
        s = out
        
        while stack :
            q = queue.pop(0)
            s.next = q
            s = stack.pop()
            q.next = s
        
        if queue :
            q = queue.pop(0)
            s.next = q
            q.next = None
            return out.next
            
        else :
            s.next = None
            return out.next
        
        
        
        
        
        