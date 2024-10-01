class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) < 2 :
            return 0
        
        elif len(nums) == 2 :
            return abs(nums[0]-nums[1])
        
        N = len(nums)-1
        D = defaultdict(list)
        minN, maxN = min(nums), max(nums)
        
        for num in nums :
            
            if num != maxN :
                idx = (num - minN) * N // (maxN-minN)
            else :
                idx = N-1
        
            D[idx].append(num)
            
        bucket_sort = []
        for i in range(N) :
            if D[i] :
                D[i].sort()
                bucket_sort += [min(D[i]), max(D[i])]
        
        #print(bucket_sort)
        diff = 0
        for i in range(len(bucket_sort) -1):
            diff = max(bucket_sort[i+1] - bucket_sort[i], diff)
            
        return diff
        
        
        
        
        
        
        
        