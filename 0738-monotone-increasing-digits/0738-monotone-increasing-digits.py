class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        n_str = list(str(n))
        N = len(n_str)

        last = N
        index = N-1

        while index > 0:

            if int(n_str[index-1]) > int(n_str[index]):
                n_str[index-1] = str(int(n_str[index-1]) -1)
                n_str[index:last] = ['9'] * (last-index)
                last = index
            index -= 1
        
        ret = int(''.join(n_str))
        return ret