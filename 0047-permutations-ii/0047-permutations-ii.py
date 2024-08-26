class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        L = len(nums)
        last = -100
        
        ans1 = [[]]
        
        for num in nums :
            
            #print(ans1)
            ans2 = []
            for tmp in ans1 :
                
                flag = False
                l = len(tmp)
                for i in range(l):
                    
                    if i == 0 :
                        new_tmp = [num] + tmp[:]
                        ans2.append(new_tmp)
                    else :
                        if flag == False :
                            new_tmp = tmp[:i] + [num] + tmp[i:]
                            ans2.append(new_tmp)
                    
                    if tmp[i] == num :
                        flag = True
                
                if l == 0 :
                    ans2.append([num])
                else :
                    if flag == False :
                        new_tmp = tmp[:] + [num]
                        ans2.append(new_tmp)
            
            ans1 = ans2[:]
        
        #print(ans1)
        return ans1     
            
        
        
        
        
        