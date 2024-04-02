class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = set()

        N, Z, P = [], [], []

        for n in nums :
            if n > 0 :
                P.append(n)
            elif n == 0 :
                Z.append(n)
            else :
                N.append(n)

        PS = set(P)
        NS = set(N)

        if len(Z) >= 3 :
            result.add((0,0,0))

        if len(Z) >= 1 :
            for p in PS :
                for n in NS:
                    if p+n == 0 :
                        result.add((0,p,n))

        for p1 in range(len(P)-1) :
            for p2 in range(p1+1, len(P)):
                if -(P[p1]+P[p2]) in NS :
                    result.add(tuple(sorted([P[p1], P[p2], -P[p1]-P[p2]])))

        for n1 in range(len(N)-1) :
            for n2 in range(n1+1, len(N)):
                if -(N[n1]+N[n2]) in PS :
                    result.add(tuple(sorted([N[n1], N[n2], -N[n1]-N[n2]])))
                    
        return result

                        