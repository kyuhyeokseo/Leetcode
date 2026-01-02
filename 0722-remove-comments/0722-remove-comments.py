class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        ret = []
        multi = 0

        for line in source:
            if multi == 0:
                tmp = ""
            
            for i in range(len(line)):
                print(line[i], multi)
                if i > 0 and line[i-1] == '*' and line[i] == '/' and multi>2:
                    multi = 0
                elif i < len(line)-1 and line[i] == '/' and line[i+1] == '/':
                    if multi == 0:
                        break
                    else:
                        pass
                elif multi == 0 and i < len(line)-1 and line[i] == '/' and line[i+1] == '*':
                    multi = 1
                else:
                    if multi == 0:
                        tmp += line[i]
                    else:
                        multi += 1
            
            if multi == 0:
                if tmp:
                    ret.append(tmp)

        return ret