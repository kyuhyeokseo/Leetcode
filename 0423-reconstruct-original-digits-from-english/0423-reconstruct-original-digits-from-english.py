class Solution:
    def originalDigits(self, s: str) -> str:

        D = {}
        for t in s :
            if t in D :
                D[t] += 1
            else :
                D[t] = 1

        cnt = [0 for _ in range(10)]
        N = [('zero', 0),('four',4),('five',5),('seven',7),('eight',8),('six',6),('two',2),('three',3),('one',1),('nine',9)]
        
        idt = ['z','u','f','v','g','x','w','t','o','e']

        for i, x in enumerate(idt):
            
            if x in D :
                n = D[x]
                if n == 0 :
                    continue
                str_num, num = N[i]
                for each_str in str_num :
                    D[each_str] -= n
                cnt[num] += n
            
        #print(cnt)

        ret = ''
        for i in range(10):
            ret += (str(i) * cnt[i])

        return ret

        # zero 'z' (0)
        # one 'o' (8)
        # two 'w' (6)
        # three 't' (7)
        # four 'u' (1)
        # five 'f' (2)
        # six 'x' (5)
        # seven 'v' (3)
        # eight 'g' (4) 
        # nine 'e' (9)