class Solution:
    def calculate(self, s: str) -> int:

        items = []
        tmp = ""
        for i in range(len(s)):
            x = s[i]
            if x in ['(', ')', '+', '-'] :
                if len(tmp) == 0 and x == '-':
                    if len(items) == 0:
                        items.append('--')
                        continue
                    elif items[-1] == '(' :
                        items.append('--')
                        continue
                    
                if len(tmp) > 0:
                    items.append(int(tmp))
                    tmp = ""
                items.append(x)
                
            elif x >= '0' and x <= '9' :
                tmp = tmp + x
        if len(tmp) > 0 :
            items.append(int(tmp))

        print(items)

        postfix = []
        stk = []
        for i in range(len(items)):
            target = items[i]
            if target == '(' :
                stk.append(target)
            elif target in ['+', '-', '--'] :
                while len(stk) != 0:
                    if stk[-1] == '(':
                        break
                    postfix.append(stk.pop())
                stk.append(target)
            elif target == ')' :
                while len(stk) != 0 :
                    if stk[-1] == '(' :
                        stk.pop()
                        break
                    postfix.append(stk.pop())
            else :
                postfix.append(target)

        while len(stk) != 0 :
            postfix.append(stk.pop())
                
        print(postfix)

        stk = []
        # do postfix calculator
        for tmp in postfix :
            if tmp in ['+', '-']:
                op2 = stk.pop()
                op1 = stk.pop()
                if tmp == '+' :
                    stk.append(op1 + op2)
                else :
                    stk.append(op1 - op2)
            elif tmp == '--' :
                op = stk.pop()
                stk.append(-op)
            else :
                stk.append(tmp)

        return stk[-1]

        
        
        