class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        
        ret = ''
        L = len(nums)

        if L == 1 :
            return str(nums[0])
        elif L == 2 :
            return str(nums[0]) + '/' + str(nums[1])
        else:
            ret += str(nums[0]) + '/' + '('
            for i in range(1, L):
                ret += str(nums[i])
                if i < L-1:
                    ret += '/'
            ret += ')'
        
        return ret