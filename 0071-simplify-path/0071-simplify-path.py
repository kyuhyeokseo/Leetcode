class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stk = []
        path_list = path.split("/")
        
        for tmp in path_list :
            
            if len(tmp) == 0:
                continue
            
            if tmp == '.' :
                continue

            elif tmp == '..':
                if len(stk) == 0 :
                    continue
                else :
                    stk.pop()
            
            else :
                stk.append(tmp)

        #print(stk)
        return '/' + '/'.join(stk)
        
        