class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        bits = bits[::-1]

        while bits:
            tmp = bits.pop()
            if tmp:
                bits.pop()
        return not tmp