# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        L, H = 1, n
        
        while True :
            
            if H - L == 1 :
                if guess(L) == 0 :
                    return L
                else :
                    return H
            
            mid = (L+H)//2
        
            if guess(mid) == -1 :
                H = mid
            elif guess(mid) == 1 :
                L = mid
            else :
                return mid
            
        
        
        