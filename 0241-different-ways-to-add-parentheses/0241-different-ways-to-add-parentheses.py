class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        E = []
        
        cnt_op = 0
        num = ''
        for i in range(len(expression)):
            
            if expression[i] in ['+', '-', '*'] :
                E.append(int(num))
                num = ''
                E.append(expression[i])
                cnt_op += 1
        
            else :
                num += expression[i]
        E.append(int(num))
        
        return self.compute(E)
        
        
        
        
    def compute(self, exp: list) -> List[int] :
        
        if len(exp) == 1 :
            return [exp[0]]
        
        ret = []
        
        L = len(exp)
        for i in range(L):
            
            if exp[i] in ['+', '-', '*']:
                
                list1 = self.compute(exp[:i])
                list2 = self.compute(exp[i+1:])
                
                #print('----------------------')
                #print(i, exp[i], list1, list2)
            
                if exp[i] == '+':
                    for n1 in list1 :
                        for n2 in list2 :
                            ret.append(n1 + n2)
                elif exp[i] == '-':
                    for n1 in list1 :
                        for n2 in list2 :
                            ret.append(n1 - n2)
                elif exp[i] == '*':
                    for n1 in list1 :
                        for n2 in list2 :
                            ret.append(n1 * n2)
        
        return ret
        
        
        
        