class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        ret = 0
        b = 1
        for _ in range(32):

            cnt0, cnt1 = 0, 0
            for num in nums :
                if num & b == b :
                    cnt1 += 1
                else :
                    cnt0 += 1
            ret += cnt0 * cnt1
            b = b << 1
        
        return ret

