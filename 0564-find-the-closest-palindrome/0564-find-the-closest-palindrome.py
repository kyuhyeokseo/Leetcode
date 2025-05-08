class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        if n in ['10', '11']:
            return '9'

        L = len(n)

        if len(n) % 2 == 0:
            W = n[L//2:]
            X = n[:L//2]
            Y = str(int(X) + 1)
            Z = str(int(X) - 1)

            X_rev, Y_rev, Z_rev = X[::-1], Y[::-1] if len(Y) == L//2 else Y[:-1][::-1], Z[::-1] if len(Z) == L//2 else "9" + Z[::-1]

            X_diff = abs(int(W) - int(X_rev))
            Y_diff = abs(int("1" + Y_rev) - int(W))
            Z_diff = abs(int("1" + W) - int(Z_rev))

            M = min(X_diff, Y_diff, Z_diff) if n != (X+X_rev) else min(Y_diff, Z_diff)

            if M == Z_diff :
                return Z+Z_rev
            elif M == X_diff and n != (X+X_rev) :
                return X+X_rev
            else :
                return Y+Y_rev
        
        elif L == 1:
            if int(n) == 0:
                return '1'
            else:
                return str(int(n) - 1)

        else:
            W = n[L//2+1:]
            X = n[:L//2+1]
            Y = str(int(X) + 1)
            Z = str(int(X) - 1)

            X_rev, Y_rev, Z_rev = X[:-1][::-1], Y[:-1][::-1] if len(Y) == L//2 + 1 else Y[:-2][::-1], Z[:-1][::-1] if len(Z) == L//2 + 1 else Z[::-1]

            X_diff = abs(int(W) - int(X_rev))
            Y_diff = abs(int("1" + Y_rev) - int(W))
            Z_diff = abs(int("1" + W) - int(Z_rev))

            M = min(X_diff, Y_diff, Z_diff) if n != (X+X_rev) else min(Y_diff, Z_diff)
            
            if M == Z_diff :
                return Z+Z_rev
            elif M == X_diff and n != (X+X_rev) :
                return X+X_rev
            else :
                return Y+Y_rev

