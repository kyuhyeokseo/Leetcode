class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        MAX = 100001
        MIN = -100001
        
        D = {}
        D_detail = {}
        S = 0
        
        LD_X, LD_Y = MAX, MAX
        RU_X, RU_Y = MIN, MIN
        
        for R in rectangles :
            
            S += (R[2] - R[0]) * (R[3] - R[1])
            
            P_list = []
            P_list.append([R[0], R[1]])
            P_list.append([R[0], R[3]])
            P_list.append([R[2], R[1]])
            P_list.append([R[2], R[3]])
            
            LD_X = min(LD_X, R[0])
            LD_Y = min(LD_Y, R[1])
            RU_X = min(RU_X, R[2])
            RU_Y = min(RU_Y, R[3])
            
            for i, p in enumerate(P_list) :
                
                key = str(p[0]) + '.' + str(p[1])
                
                key_detail = key
                if i == 0 :
                    key_detail += '.LD'
                elif i == 1 :
                    key_detail += '.LU'
                elif i == 2 :
                    key_detail += '.RD'
                elif i == 3 :
                    key_detail += '.RU'
                
                
                if key in D :
                    if D[key] == 1 :
                        del D[key]
                    else :
                        return False
                else :
                    D[key] = 1
                    
                if key_detail in D_detail :
                    return False
                else :
                    D_detail[key_detail] = True

        if len(D.keys()) != 4 :
            return False
        
        for v in D.values():
            if v != 1 :
                return False
        
        sX, sY = set(), set()
        for k in D.keys():
            tmp = k.split('.')
            sX.add(int(tmp[0]))
            sY.add(int(tmp[1]))
        
        if len(list(sX)) == 2 and len(list(sY)) == 2 :
            return S == ((max(sX) - min(sX)) * (max(sY) - min(sY)))
            
        else :
            return False
            
        
        
        
        
        
        