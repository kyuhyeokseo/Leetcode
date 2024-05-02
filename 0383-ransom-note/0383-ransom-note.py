class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rd, md = {}, {}
        for i in range(len(ransomNote)):
            target = ransomNote[i]
            if target in rd :
                rd[target] += 1
            else :
                rd[target] = 1
        for j in range(len(magazine)):
            target = magazine[j]
            if target in md :
                md[target] += 1
            else :
                md[target] = 1
        
        for k in rd.keys():
            if k not in md :
                return False
            elif md[k] < rd[k]:
                return False
            
        return True