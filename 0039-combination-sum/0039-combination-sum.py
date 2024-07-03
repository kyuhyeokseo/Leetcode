class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort(reverse= True)
        
        ret = []
        
        ans = [[0]]
        
        for num in candidates :
            #print(f'\n------- {num} --------')
            
            tmp = []
            #print(ans)
            #print(ret)
            for a in ans :
                
                if a[0] == 0 :
                    a_copy = a[:]
                    for t in range(0, target//num + 1) :
                        if t == 0 :
                            tmp.append(a_copy[:])
                        else :
                            a_copy[0] += num
                            if a_copy[0] > target :
                                continue
                            elif a_copy[0] == target :
                                a_copy.append(num)
                                ret.append(a_copy[1:])
                            else :
                                a_copy.append(num)
                                tmp.append(a_copy[:])
                else :
                    a_copy = a[:]
                    for t in range(0, target//num + 1) :
                        if t == 0 :
                            tmp.append(a_copy[:])
                        else :
                            a_copy[0] += num
                            if a_copy[0] > target :
                                continue
                            elif a_copy[0] == target :
                                a_copy.append(num)
                                ret.append(a_copy[1:])
                            else :
                                a_copy.append(num)
                                tmp.append(a_copy[:])

            ans = tmp[:]
            
        return ret
        
        
        