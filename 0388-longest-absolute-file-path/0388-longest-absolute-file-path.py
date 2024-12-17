class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        def is_file(name):
            tmp = name.split('.')
            if len(tmp) > 1 :
                return True
            else :
                return False
        
        
        X = input.split('\n')
        
        #if len(X) == 1 :
        #    if is_file(X[0]) :
        #        return len(X[0])
        #    else :
        #        return 0
        
        D = {}
        ret = 0
        
        for item in X :
            
            A = item.lstrip('\t')
            level = (len(item) - len(A))
            
            #print(f'------ {item, A, level} ------\n')
            
            if level == 0 :
                if is_file(A) :
                    ret = max(ret, len(A))
                else :
                    D[level] = len(A) + 1
            else :
                if is_file(A) :
                    ret = max(ret, D[level-1] + len(A))
                else :
                    D[level] = D[level-1] + len(A) + 1
            
            #print(ret)
            #print(D)
        
        return ret
        
        
        
        
        
        
        