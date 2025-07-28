class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        N, K = len(nums), k
        dp = [[(-1,-1), (-1,-1,-1), (-1,-1,-1,-1)] for _ in range(N)]

        dp[K-1][0]   = (sum(nums[:K]), 0)
        dp[2*K-1][1] = (sum(nums[:2*K]), 0, K)
        dp[3*K-1][2] = (sum(nums[:3*K]), 0, K, 2*K)

        for k in range(K, N):
            M = max(dp[k-1][0][0], sum(nums[k-K+1:k+1]))
            if M == dp[k-1][0][0]:
                dp[k][0] = (M, dp[k-1][0][1])
            else:
                dp[k][0] = (M, k-K+1)
            
        
        for k in range(2*K, N):
            M = max(dp[k-1][1][0], dp[k-K][0][0] + sum(nums[k-K+1:k+1]))
            if M == dp[k-1][1][0]:
                dp[k][1] = (M,) + dp[k-1][1][1:]
            else:
                dp[k][1] = (M, dp[k-K][0][1], k-K+1)

        for k in range(3*K, N):
            M = max(dp[k-1][2][0], dp[k-K][1][0] + sum(nums[k-K+1:k+1]))
            if M == dp[k-1][2][0]:
                dp[k][2] = (M,) + dp[k-1][2][1:]
            else:
                dp[k][2] = (M,) + dp[k-K][1][1:] + (k-K+1,)



        #for k in range(N):
        #    print(dp[k][0], dp[k][1], dp[k][2])
        

        return list(dp[-1][2][1:])
        