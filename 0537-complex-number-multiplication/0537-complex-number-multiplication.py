class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        z1, z2 = num1.split('+'), num2.split('+')
        r1, i1 = int(z1[0]), int(z1[1][:-1])
        r2, i2 = int(z2[0]), int(z2[1][:-1])

        print(r1, i1, r2, i2)

        R = r1 * r2 - i1 * i2
        I = r1 * i2 + i1 * r2

        return str(R) + '+' + str(I) + 'i'