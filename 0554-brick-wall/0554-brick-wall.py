class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        D = {}
        SUM = sum(wall[0])
        MAX = 0
        N = len(wall)

        for rows in wall:
            s = 0
            for w in rows:
                s += w
                if s < SUM and s in D:
                    D[s] += 1
                    MAX = max(MAX, D[s])
                elif s < SUM :
                    D[s] = 1
                    MAX = max(MAX, D[s])
        
        return N - MAX
            





