class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            target = 1 << i
            mask |= target

            S = set([mask & n for n in nums])

            ans_tmp = ans | target
            for s in S :
                if ans_tmp ^ s in S :
                    ans = ans_tmp
                    break
            
        return ans
            
