# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        
        randN = 40
        while randN >= 40 :
            randN = 7*(rand7() - 1) + (rand7()-1)
        return randN % 10 + 1
        
        