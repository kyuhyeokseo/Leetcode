class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        ans = []
        
        def FindOperate(idx, path, result, tmpNum):
            
            if idx == len(num) :
                if result == target :
                    ans.append(path)
                return True
            
            for j in range(idx, len(num)):
                
                if j>idx and num[idx] == '0':
                    break
                
                N = int(num[idx:j+1])
                
                if idx == 0 :
                    FindOperate(j+1, path + str(N), result + N, N)
                else :
                    FindOperate(j+1, path + '+' + str(N), result + N, N)
                    FindOperate(j+1, path + '-' + str(N), result - N, -N)
                    FindOperate(j+1, path + '*' + str(N), result - tmpNum + tmpNum * N, tmpNum * N)
                    
        FindOperate(0, '', 0, 0)   
        return ans
                