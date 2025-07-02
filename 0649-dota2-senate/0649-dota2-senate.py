class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        N = len(senate)

        R, D = 0, 0
        banR, banD = 0, 0
        for s in senate:
            if s == 'R':
                R+=1
            else:
                D+=1
        
        senate = list(senate)

        while R and D:
            t = senate.pop(0)
            if   t == 'R' and banR > 0:
                banR -= 1
                R -= 1
            elif t == 'R' and banR == 0:
                banD += 1
                senate.append('R')
            elif t == 'D' and banD > 0:
                banD -= 1
                D -= 1
            elif t == 'D' and banD == 0:
                banR += 1
                senate.append('D')
            
            #print(t, senate, R, D, banR, banD)
            
            if not (R and D):
                break

        if R:
            return 'Radiant'
        else:
            return 'Dire'
