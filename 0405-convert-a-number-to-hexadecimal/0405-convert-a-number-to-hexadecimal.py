class Solution:
    def toHex(self, num: int) -> str:

        standard = 15
        ret = ''

        for _ in range(8):
            
            a = num & standard
            num = num >> 4

            ret = (str(a) if a < 10 else chr(ord('a') + a - 10)) + ret
        ret = ret.lstrip('0')

        return '0' if ret == '' else ret
        








