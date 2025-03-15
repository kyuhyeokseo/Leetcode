class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        D = {}
        
        q = []

        for n in nums2:
            if len(q) == 0:
                q.append(n)
            else:
                while q and q[-1] < n:
                    last = q.pop()
                    D[last] = n
                q.append(n)
        while q:
            last = q.pop()
            D[last] = -1
        
        
        ret = []
        for n in nums1:
            ret.append(D[n])

        return ret
