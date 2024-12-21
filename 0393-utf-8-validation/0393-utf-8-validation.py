class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        
        L = len(data)
        B = 1
        
        for i in range(L):
            
            if B == 1 :
                if data[i] & 0b10000000 == 0b00000000 :
                    B = 1
                elif data[i] & 0b11100000 == 0b11000000 :
                    B = 2
                elif data[i] & 0b11110000 == 0b11100000 :
                    B = 3
                elif data[i] & 0b11111000 == 0b11110000 :
                    B = 4
                else :
                    return False
            
            elif B > 1 :
                if data[i] & 0b11000000 == 0b10000000 :
                    B -= 1
                else :
                    return False
        
        return B == 1
            
        
        
        
        