class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        ret = []
        L1, L2 = len(list1), len(list2)

        for s in range(0, L1+L2-1):
            for s1 in range(max(0, s-L2+1), min(s+1,L1)):
                s2 = s - s1
                if list1[s1] == list2[s2]:
                    ret.append(list1[s1])
            if ret:
                return ret
        
        return []