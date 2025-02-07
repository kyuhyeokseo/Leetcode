class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        N = len(nums1)
        ret = 0

        First = {}
        for i in range(N):
            for j in range(N):
                S = nums1[i] + nums2[j]
                if -S in First :
                    First[-S] += 1
                else :
                    First[-S] = 1
        
        for k in range(N):
            for l in range(N):
                S = nums3[k] + nums4[l]
                if S in First :
                    ret += First[S]

        return ret
