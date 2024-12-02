from collections import defaultdict

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        A = defaultdict(list)
        P = defaultdict(list)
        
        for i in nums:
            P[i] = [i]
            for j in nums :
                if i > j and i % j == 0 :
                    A[j].append(i)
        
        end = nums[:]
        
        while True :
            
            tmp = set()
            for n in end :
            
                path = P[n]

                for nei in A[n]:
                    P[nei] = path[:] + [nei]
                    tmp.add(nei)
                        
            end = list(tmp)
            if len(end) == 0:
                break
        
        ans = [nums[0]]
        for n in nums :
            
            #print(P[n])
            
            if len(P[n]) > len(ans):
                ans = P[n]
        return ans
                
        
        
        
        
        