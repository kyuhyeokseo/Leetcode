class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        M, N = len(image), len(image[0])
        TARGET = image[sr][sc]

        if TARGET == color:
            return image
        
        currs = [(sr, sc)]

        while currs:
            m, n = currs.pop(0)
            image[m][n] = color
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                x, y = m+dx, n+dy
                if 0<=x<M and 0<=y<N:
                    if image[x][y] == TARGET:
                        currs.append((x,y))
        
        return image




