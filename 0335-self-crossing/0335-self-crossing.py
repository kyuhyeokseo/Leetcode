class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        
        L = len(distance)
        
        if L < 3 :
            return False
        
        for i in range(3, L):
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3] :
                print('a : ', i)
                return True
            
            if i>=4 :
                if distance[i-1] == distance[i-3] and distance[i-2] > distance[i-4] and distance[i-2] <= distance[i-4] + distance[i]:
                    print('b : ', i)
                    return True
            
            if i>=5 :
                if distance[i] + distance[i-4] >= distance[i-2] and distance[i-1] + distance[i-5] >= distance[i-3] and distance[i-2] >= distance[i-4] and distance[i-3] >= distance[i-5] and distance[i-2] >= distance[i] and distance[i-3] >= distance[i-1]:
                    print('c : ', i)
                    return True
        
        return False
                
            
        
        
        
        
        
        