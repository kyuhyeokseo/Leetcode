class Solution:
    
    def __init__(self):
        
        self.X = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        self.Y = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.Z = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    
    def numberToWords(self, num: int) -> str:
    
        if num == 0 :
            return 'Zero'
        
        billion = num // (10**9)
        num = num % (10 ** 9)
        million = num // (10**6)
        num = num % (10**6)
        thousand = num // (10**3)
        num = num % (10**3)
        
        B = self.n2w_thousand(billion)
        M = self.n2w_thousand(million)
        K = self.n2w_thousand(thousand)
        O = self.n2w_thousand(num)
        
        ret = ''
        if B != '':
            ret += (B + ' Billion')
        if M != '':
            ret += (' ' + M + ' Million')
        if K != '':
            ret += (' ' + K + ' Thousand')
        if O != '':
            ret += (' ' + O)
        return ret.strip()
        

    def n2w_thousand(self, n):
        
        if n == 0 :
            return ''
        
        ret = ''
        
        hundred = n // 100
        n = n % 100
        
        if self.X[hundred] != '':
            ret += (self.X[hundred] + ' Hundred')

        if n == 0 :
            pass
        elif n < 10 :
            ret += (' ' + self.X[n])
        elif n == 10 :
            ret += ' Ten'
        elif n < 20 :
            ret += (' ' + self.Z[n%10])
        else :
            ret += (' ' + self.Y[n//10] + ' ' + self.X[n%10])
        return ret.strip()
            
        
        
        
        
        