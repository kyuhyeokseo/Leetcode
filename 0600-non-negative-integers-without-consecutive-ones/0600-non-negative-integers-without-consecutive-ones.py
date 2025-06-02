class Solution:
    def findIntegers(self, n: int) -> int:
        
        if n == 1: return 2
        if n == 2: return 3
        if n == 3: return 3
        if n == 4: return 4
        if n == 5: return 5
        if n == 6: return 5
        if n == 7: return 5

        cum = [1,2]
        # dp[i]: # of valid binary expressions of length i starting wtih 1
        # dp[3] = 2 (ex.101, 100)

        for _ in range(28):
            cum.append(cum[-1]+cum[-2])

        #print(f'{n:32b}')
        #print(cum[::-1])
        #print(len(cum))
        ret = 0
        flag = False
        for j in range(len(cum)-1, -1, -1):
            if (1<<j) & n:
                ret += cum[j]
                if flag:
                    return ret
                flag = True
            else :
                flag = False

        return ret + 1


