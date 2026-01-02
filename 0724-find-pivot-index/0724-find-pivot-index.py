class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left, right = [0], [0]
        N = len(nums)

        if N == 1:
            return 0

        for i in range(N-1):
            left.append(left[-1] + nums[i])
            right = [right[0] + nums[N-1-i]] + right[:]
        
        for i in range(N):
            if left[i] == right[i]:
                return i
        
        return -1
