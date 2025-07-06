class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        L, U = 0, 0

        for m in moves:
            if m == 'L':
                L += 1
            elif m == 'R':
                L -= 1
            elif m == 'D':
                U -= 1
            else:
                U += 1
        
        return not L and not U