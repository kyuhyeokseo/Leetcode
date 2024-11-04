class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        L = len(nums)
        ret = [0 for _ in range(L)]
        X = list(enumerate(nums))
        
        
        def operate(X):
            
            mid = len(X) // 2
            
            if mid > 0 :
                
                left = operate(X[:mid])
                right = operate(X[mid:])
                #print(left, right)
                
                for i in range(len(X))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        ret[left[-1][0]] += len(right)
                        X[i] = left.pop()
                    else :
                        X[i] = right.pop()
            
            return X
                        
        
        operate(X)
        return ret
            
            
            