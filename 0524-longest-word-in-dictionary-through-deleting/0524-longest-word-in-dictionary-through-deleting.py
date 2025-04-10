class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        dictionary.sort()
        checks = [0 for _ in range(len(dictionary))]

        for i in range(len(s)):
            target = s[i]
            for j, check in enumerate(checks):
                if check < len(dictionary[j]):
                    if target == dictionary[j][check]:
                        checks[j] += 1
        
        ret = ''
        for j, check in enumerate(checks):
            if check == len(dictionary[j]):
                if len(ret) < check:
                    ret = dictionary[j]
        
        return ret