class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        diff = abs(-10002 - x)
        I = -1
        for i, n in enumerate(arr):
            if abs(n-x) < diff:
                diff = abs(n-x)
                I = i
        
        #print(I)

        befs, afts = arr[:I+1][::-1], arr[I+1:]

        ret1, ret2 = [], []

        for _ in range(k):
            if befs and afts:
                if abs(x-befs[0]) <= abs(x-afts[0]):
                    ret1.append(befs[0])
                    befs.pop(0)
                else:
                    ret2.append(afts[0])
                    afts.pop(0)
            elif befs and not afts:
                ret1.append(befs[0])
                befs.pop(0)
            else:
                ret2.append(afts[0])
                afts.pop(0)

        #print(ret1,ret2)

        return ret1[::-1] + ret2[:]
