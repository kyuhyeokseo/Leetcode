class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        tmp1 = [[]]
        
        for num in nums :
            
            tmp2 = []
            for item in tmp1 :
                print(item)
                L = len(item)
                
                if L == 0 :
                    tmp2.append(item[:] + [num])
                elif L == 1:
                    tmp2.append(item[:] + [num])
                    tmp2.append([num] + item[:])
                else :
                    tmp2.append(item[:] + [num])
                    
                    for i in range(1, L):
                        tmp2.append(item[:i] + [num] + item[i:])
                    
                    tmp2.append([num] + item[:])
            print(tmp2)
        
            tmp1 = tmp2[:]
            
        return tmp1