class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        adj = defaultdict(list)
        rec = {}

        ret = []

        for i, account in enumerate(accounts):
            account = [account[0]] + list(set(account[1:]))
            for email in account[1:]:
                if email in rec:
                    j = rec[email]
                    adj[j].append(i)
                    adj[i].append(j)
                else:
                    rec[email] = i
        
        N = len(accounts)
        visited = [False] * N

        idx = 0
        groups = {}

        for i in range(N):
            tmp = []
            if visited[i] == False:
                currs = [i]
                while currs:
                    curr = currs.pop(0)
                    tmp.append(curr)
                    visited[curr] = True
                    if curr in adj:
                        adj_list = list(set(adj[curr]))
                    else:
                        adj_list = []
                    for nei in adj_list:
                        if visited[nei] == False:
                            currs.append(nei)
                groups[idx] = tmp[:]
                idx += 1

        #print(groups)
        
        ret = []
        for key, value in groups.items():
            ret.append([accounts[value[0]][0]])
            email_list = [email for i in value for email in accounts[i][1:]]
            ret[-1] += sorted(list(set(email_list)))


        return ret

        




