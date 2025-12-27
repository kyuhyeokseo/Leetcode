class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        
        N = len(positions)
        height = [0] * N
        visited = [False] * N

        for idx, (x, h) in enumerate(positions):
            height[idx] += h
            for offset, (x2, h2) in enumerate(positions[idx+1:]):
                idx2 = idx + offset + 1
                if x2< x+h and x < x2+h2:
                    height[idx2] = max(height[idx2], height[idx])
        
        ret = []
        for h in height:
            ret.append(max(h, ret[-1])) if ret else ret.append(h)
        
        return ret


