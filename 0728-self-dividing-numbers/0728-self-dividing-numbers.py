class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        ret = []
        for target in range(left, right+1):
            
            flag = True
            #print(target)
            for idx in range(len(str(target))):
                n = int(str(target)[idx])
                if (n == 0) or (n and target % n) :
                    flag = False
                    break
            
            #print(flag)
            #print()
            if flag:
                ret.append(target)
        
        return ret