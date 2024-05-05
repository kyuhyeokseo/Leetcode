class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stk = []
        L = len(tokens)
        for i in range(L):
            tmp = tokens[i]
            if tmp in ['+', '-', '*', '/'] :
                op2 = stk.pop()
                op1 = stk.pop()
                if tmp == '+' :
                    stk.append(op1 + op2)
                elif tmp == '-' :
                    stk.append(op1 - op2)
                elif tmp == '*' :
                    stk.append(op1 * op2)
                else :
                    stk.append(int(op1 / op2))
            else :
                stk.append(int(tmp))
            #print(stk)

        return stk.pop()
        
        
        