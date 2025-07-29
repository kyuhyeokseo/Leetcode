class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        N, K = len(nums), k

        left, right = [[-1, -1] for _ in range(N)], [[-1, -1] for _ in range(N)]

        for n in range(k, N-2*K+1):
            M = max(left[n-1][0], sum(nums[n-K:n]))
            if M == left[n-1][0]:
                left[n] = [M, left[n-1][1]]
            else:
                left[n] = [M, n-K]
            
            x = N-1-n
            M = max(right[x+1][0], sum(nums[x+1:x+K+1]))
            if M == sum(nums[x+1:x+K+1]):
                right[x] = [M, x+1]
            else:
                right[x] = [M, right[x+1][1]]
            
        #print(left)
        #print(right)

        M = -1
        ret = None
        for b in range(K, N-2*K+1):
            if M < left[b][0] + sum(nums[b:b+K]) + right[b+K-1][0]:
                M = left[b][0] + sum(nums[b:b+K]) + right[b+K-1][0]
                ret = [left[b][1], b, right[b+K-1][1]]
        
        return ret
        