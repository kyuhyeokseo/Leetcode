class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1 :
            return 9
        
        ret = 0
        min_num, max_num = 10 ** (n-1), 10 ** n - 1

        for i in range(max_num, min_num-1, -2):

            if i * i < ret :
                break
            
            for j in range(max_num, i-1, -2):
                tmp = i * j

                if tmp % 11 != 0 and tmp > ret :
                    continue

                if str(tmp) == str(tmp)[::-1]:
                    ret = tmp
        
        return ret % 1337