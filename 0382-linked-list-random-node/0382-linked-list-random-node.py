# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        idx = 1
        out = 0
        curr = self.head
        
        while curr :
            if random.randint(1,idx) == 1:
                out = curr.val
            idx += 1
            curr = curr.next
        return out


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()