class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        D = {}

        odd = 0
        ret = 0

        for x in s :
            if x in D :
                del D[x]
                odd -= 1
                ret += 2
            else :
                D[x] = 1
                odd += 1
        
        if odd :
            return ret + 1
        else :
            return ret





