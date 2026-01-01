class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        adj = {}
        rec = {}

        ret = []

        for i, account in enumerate(accounts):
            flag = -1
            for email in account[1:]:
                if email in rec:
                    flag = rec[email]
                    break
            
            if flag >= 0:
                for email in account[1:]:
                    rec[email] = flag
                    ret[flag].append(email)
                ret[flag] = [ret[flag][0]] + sorted(list(set(ret[flag][1:])))
            else:
                ret.append([account[0]])
                for email in account[1:]:
                    rec[email] = len(ret)-1
                    ret[-1].append(email)
                ret[-1] = [ret[-1][0]] + sorted(list(set(ret[-1][1:])))

        return ret

        




