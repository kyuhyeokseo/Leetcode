import heapq

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compareNum(m, n):
            M, N = int(str(m) + str(n)), int(str(n) + str(m))
            
            if M > N :
                return 1
            elif M == N :
                return 0
            else :
                return -1
            
        
        L = len(nums)
        if L == 1 :
            return str(nums[0])
        
        for level in range(1, L):
            
            for j in range(level, 0, -1) :
                if compareNum(nums[j], nums[j-1]) == 1 :
                    nums[j], nums[j-1] = nums[j-1], nums[j]
        
        #print(nums)
        out = ''
        for i in nums :
            out += str(i)
        return str(int(out))
            
        
        
        
        
        