class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        nums.append(1)
        nums = [1] + nums
        
        M = [[0 for _ in range(N+2)] for _ in range(N+2)]
        
        for i in range(1, N+1):
            M[i][i] = nums[i-1] * nums[i] * nums[i+1]
        
        for diff in range(1, N):
            for srt in range(1, N+1-diff):
                
                end = srt + diff
                tmp = -1

                for k in range(srt, end+1):
                    tmp = max(tmp, M[srt][k-1] + M[k+1][end] + nums[srt-1]*nums[k]*nums[end+1])
        
                M[srt][end] = tmp
        
        #for item in M:
        #    print(item)
        
        return M[1][N]
        
        
        