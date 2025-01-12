class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        
        L = len(password)
        lower, upper, digit = 0,0,0
        repeat = []

        one = two = 0

        prev, r = '', 0

        for i in range(L):

            curr = password[i]
            if 'a' <= curr <= 'z':
                lower += 1
            elif 'A' <= curr <= 'Z':
                upper += 1
            elif '0' <= curr <= '9':
                digit += 1
            
            if curr == prev :
                r += 1
            else :
                if r >= 3 :
                    repeat.append(r)
                    if r % 3 == 0 :
                        one += 1
                    elif r % 3 == 1 :
                        two += 1
                r = 1
            prev = curr
            
            if i == L-1 and r >= 3 :
                repeat.append(r)
                if r % 3 == 0 :
                    one += 1
                elif r % 3 == 1 :
                    two += 1

        least = (1 if lower == 0 else 0) + (1 if upper == 0 else 0) + (1 if digit == 0 else 0)
        
        rep = 0
        for t in repeat :
            rep += t//3

        if L < 6 :
            return max(6-L, least, rep)
        
        elif L > 20 :
            
            rep -= min(L-20, one)
            rep -= min(max(L-20-one, 0), two * 2) // 2
            rep -= max(L-20-one-2*two, 0) // 3

            return (L-20) + max(least, rep)
        
        else :
            #print(repeat, rep, least)
            return max(rep, least)






