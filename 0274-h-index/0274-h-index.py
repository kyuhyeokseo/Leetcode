class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        L = len(citations)
        citations.sort(reverse=True)

        for i in range(L):

            if (i+1) >= citations[i]:
                return max(citations[i], i)
            
        return L