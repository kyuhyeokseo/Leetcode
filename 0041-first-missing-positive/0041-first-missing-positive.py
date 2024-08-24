class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        N = len(nums)
        
        check_list = [False for _ in range(N+2)]
        
        for n in nums :
            if n < 1 :
                check_list = check_list[:-1]
                continue
            else :
                if n < len(check_list):
                    check_list[n] = True
        
        L = len(check_list)
        for i in range(1, L):
            if check_list[i] == False :
                return i
        
        
        
        