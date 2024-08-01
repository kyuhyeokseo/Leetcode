class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        L = len(s)
        
        checkpoint = [0]
        
        for i in range(1,L) :
            
            for srt in checkpoint :
            
                tmp = s[srt:i]
            
                if tmp in wordDict :
                    checkpoint.append(i)
                    break
        
        
        for srt in checkpoint :
            
            tmp = s[srt:]
            
            if tmp in wordDict :
                return True
            
        return False
        
        
        
        
        