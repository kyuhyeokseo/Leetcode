class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        
        dp = []

        for i in range(len(s2)):
            srt, cnt = i, 0
            for j in range(len(s1)):
                if s1[j] == s2[srt]:
                    srt += 1
                    if srt == len(s2):
                        srt = 0
                        cnt += 1
            
            dp.append((srt, cnt))
        
        idx, cnt = 0, 0
        for _ in range(n1):
            cnt += dp[idx][1]
            idx = dp[idx][0]
        
        return cnt // n2