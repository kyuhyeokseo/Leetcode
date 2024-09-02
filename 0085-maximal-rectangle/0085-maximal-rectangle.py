class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        M = len(matrix)
        N = len(matrix[0])
        out = 0
        
        heights = [0 for _ in range(N+1)]
        for y in range(M):
            
            for x in range(N):
                if matrix[y][x] == '1' :
                    heights[x] += 1
                else :
                    heights[x] = 0
            
            A = self.largest_Histogram(heights[:])
            out = max(out, A)
        
        return out
        
        
        
    def largest_Histogram(self, heights):
        N = len(heights)
        
        MAX_A = 0
        stack = []
        
        for i in range(N+1):
            
            new_H = 0 if i == N else heights[i]
            
            #print('-----------------')
            #print(i, new_H)
            
            while len(stack) > 0 and new_H < heights[stack[-1]] :
                
                
                I = stack.pop()
                W = i-stack[-1]-1 if stack else i
                H = heights[I]
                A = W * H
                #print(I, W, H, A)
                MAX_A = max(MAX_A, A)
            
            stack.append(i)
        
        
        return MAX_A