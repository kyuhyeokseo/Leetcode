class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        
        if x+y == target or x == target or y == target :
            return True
        
        if x+y < target :
            return False
        
        G = 1
        S = min(x,y)
        
        for n in range(1, S+1):
            if x%n == 0 and y%n == 0 :
                G = n
            #print(n, x%n == 0, y%n == 0, G)

        #print(target, G, target % G == 0)
        
        return target % G == 0
        
        
        
        