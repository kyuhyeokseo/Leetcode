class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        if bits[-1] != 0:
            return False

        def isPossible(bits):
            
            if not bits:
                return True
            else:
                if bits[0] == 0:
                    return isPossible(bits[1:])
                else:
                    if len(bits) == 1:
                        return False
                    else:
                        return isPossible(bits[2:])

        return isPossible(bits[:-1])