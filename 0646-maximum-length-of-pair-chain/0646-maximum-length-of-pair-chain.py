class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs = sorted(pairs, key=lambda x : (x[1], -x[0]))

        last = -1023
        cnt = 0

        while pairs:
            x = pairs.pop(0)
            if x[0] > last:
                last = x[1]
                cnt += 1
        
        return cnt