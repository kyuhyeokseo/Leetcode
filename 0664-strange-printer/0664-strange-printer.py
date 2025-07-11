class Solution:

    def __init__(self):
        self.s = None

    def strangePrinter(self, s: str) -> int:
        self.s = s
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.Util(0, n-1, dp)
    
    def Util(self, I, J, dp):
        if I>J:
            return 0
        
        if dp[I][J] != -1:
            return dp[I][J]
        
        first_letter = self.s[I]

        answer = 1 + self.Util(I+1, J, dp)
        for i in range(I+1, J+1):
            if self.s[i] == first_letter:
                better = self.Util(I, i-1, dp) + self.Util(i+1, J, dp)
                answer = min(better, answer)
        
        dp[I][J] = answer
        return answer
        