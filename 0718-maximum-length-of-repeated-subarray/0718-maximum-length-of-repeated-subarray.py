class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        M, N = len(nums1), len(nums2)

        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        ret = 0

        for m in range(M-1, -1, -1):
            for n in range(N-1, -1, -1):
                
                if nums1[m] == nums2[n]:
                    dp[m][n] = dp[m+1][n+1] + 1
                else:
                    dp[m][n] = 0
                ret = max(ret, dp[m][n])
        return ret
