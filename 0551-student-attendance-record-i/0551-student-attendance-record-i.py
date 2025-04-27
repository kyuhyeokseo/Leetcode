class Solution:
    def checkRecord(self, s: str) -> bool:
        
        A_cnt, L_cnt = 0, 0

        for t in s:
            if t == 'L':
                L_cnt += 1
                if L_cnt == 3:
                    return False

            elif t == 'A':
                A_cnt += 1
                L_cnt = 0
                if A_cnt == 2:
                    return False
            
            elif t == 'P':
                L_cnt = 0
        
        return True