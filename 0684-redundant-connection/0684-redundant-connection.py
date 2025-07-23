class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        N = len(edges)
        visited = [0 for _ in range(N)]
        D = defaultdict(list)

        id = 1

        for e in edges:
            u, v = e[0], e[1]

            D[u].append(v)
            D[v].append(u)

            if visited[u-1] == 0 and visited[v-1] == 0:
                visited[u-1] = visited[v-1] = id
                id += 1

            elif visited[u-1] == 0 and visited[v-1] > 0:
                visited[u-1] = visited[v-1]

            elif visited[v-1] == 0 and visited[u-1] > 0:
                visited[v-1] = visited[u-1]
                
            elif visited[u-1] and visited[v-1]:

                if visited[u-1] == visited[v-1]:
                    return [u, v]
                
                else:
                    VAL = visited[u-1]
                    currs = [v]
                    while currs:
                        t = currs.pop()
                        visited[t-1] = VAL
                        for nxt in D[t]:
                            if visited[nxt-1] != VAL:
                                currs.append(nxt)
                        #print(f'CURRS: {currs}')
            
            #print(e)
            #print(D)
            #print(visited)
            #print('-' * 25)
            #print()
        
        return [-1, -1]
            
            

            
            