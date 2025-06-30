class Solution:
    def solveEquation(self, equation: str) -> str:
        
        flag = 1
        N = 1
        Right = False
        num = ''

        Lin, Const = 0, 0

        for i in range(len(equation)):

            if equation[i] == '+':
                flag = 1
            elif equation[i] == '-':
                flag *= -1
            elif equation[i] == 'x':
                if not Right:
                    Lin += flag * N
                    flag, N = 1, 1
                else:
                    Lin -= flag * N
                    flag, N = 1, 1
            elif equation[i] == '=':
                Right = True
            else:
                num = num + equation[i]
                if i == len(equation)-1:
                    N = int(num)
                    num = ''
                    Const += flag * N if Right else (-flag * N)
                    flag, N = 1, 1
                elif equation[i+1] in ['+','-','=']:
                    N = int(num)
                    num = ''
                    Const += flag * N if Right else (-flag * N)
                    flag, N = 1, 1
                elif equation[i+1] == 'x':
                    N = int(num)
                    num = ''
            
        #    print(f'EQUATION : {equation[i]}, Linear: {Lin}, Constant: {Const}, FLAG: {flag}, N: {N}, RIGHT TERM: {Right}, NUM: {num}')
        
        #print(Lin, Const)

        if not Lin and not Const:
            return 'Infinite solutions'
        elif not Lin and Const:
            return 'No solution'
        else:
            return f'x={int(Const/Lin)}'

                