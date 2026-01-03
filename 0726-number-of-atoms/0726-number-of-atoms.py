class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        i, N = 0, len(formula)

        count = Counter()
        stack = [count]

        while i < N:

            if formula[i] == '(':
                i += 1
                count = Counter()
                stack.append(count)
            
            elif formula[i] == ')':
                i += 1
                srt = i

                while i < N and formula[i].isdigit():
                    i += 1

                num = int(formula[srt:i] or 1)
                top = stack.pop()

                for name, c in top.items():
                    stack[-1][name] += c * num
                
                count = stack[-1]
            
            else:
                srt = i
                i += 1
                while i < N and formula[i].islower():
                    i += 1
                AtomName = formula[srt:i]

                srt = i
                while i < N and formula[i].isdigit():
                    i += 1
                AtomCount = int(formula[srt:i] or 1)

                stack[-1][AtomName] += AtomCount
            
        ret = ''
        for name in sorted(count):
            ret += (name + (str(count[name]))) if count[name] > 1 else (name)
        
        return ret


