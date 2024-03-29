class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        L = len(gas)
        tmp = 0
        start = 0

        for i in range(L):
            tmp += gas[i] - cost[i]
            if tmp < 0:
                start = i+1
                tmp = 0
        
        t = 0
        for i in range(L):
            t += gas[(start+i)%L] - cost[(start+i)%L]
            if t<0 :
                return -1
        return start
            
            
        
        
        
        
        
        
        
        
        
        