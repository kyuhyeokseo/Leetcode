class Solution:
    def numDecodings(self, s: str) -> int:
        
        LARGE = 10 ** 9 + 7
        L = len(s)
        dp = [0] * (L+1)
        dp[0] = 1

        if s[0] == '0':
            return 0
        elif s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1

        if L == 1:
            return dp[-1]

        for i in range(1,L):
            if s[i] == '0':
                if s[i-1] in ['1', '2']:
                    dp[i+1] += (dp[i-1])
                elif s[i-1] == '*':
                    dp[i+1] += (2 * dp[i-1])
                else:
                    return 0
            elif s[i] == '*':
                dp[i+1] += (dp[i] * 9)
                if s[i-1] == '1':
                    dp[i+1] += (9 * dp[i-1])
                elif s[i-1] == '2':
                    dp[i+1] += (6 * dp[i-1])
                elif s[i-1] == '*':
                    dp[i+1] += (15 * dp[i-1])
            else:
                dp[i+1] += dp[i]
                if s[i-1] == '1':
                    dp[i+1] += (1 * dp[i-1])
                elif s[i-1] == '2' and ('1'<=s[i] and s[i]<='6'):
                    dp[i+1] += (1 * dp[i-1])
                elif s[i-1] == '*':
                    if '1'<=s[i] and s[i]<='6':
                        dp[i+1] += (2 * dp[i-1])
                    else: 
                        dp[i+1] += (1 * dp[i-1])
            
            dp[i+1] = dp[i+1] % LARGE

        #print(dp)


        return dp[-1]

