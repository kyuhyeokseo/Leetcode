class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {}
        for n in nums1 :
            if n in d :
                d[n] += 1
            else :
                d[n] = 1
        
        ans = []
        for n in nums2 :
            if n in d :
                if d[n] > 0 :
                    d[n] -= 1
                    ans.append(n)
        
        return ans
        
        
        
        