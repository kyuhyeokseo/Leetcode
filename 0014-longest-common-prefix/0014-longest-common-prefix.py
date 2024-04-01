class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ""
        L = 300

        for item in strs : 
            L = min(L, len(item))
            
        for i in range(L):
            target = strs[0][i]
            for item in strs :
                if target != item[i] :
                    return common
            common = common + target
        return common
            
            
            
            