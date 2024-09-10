class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        L = len(s)
        
        if L < 4 or L > 12 :
            return []
        
        out = [""]
        
        for level in range(4):
            
            out_tmp = []
            for Z in out :
                out_tmp.append(Z[:])
            out = []
            
            #print(out_tmp)
            for IP in out_tmp :
                
                for l in range(1,4):
                    IP_tmp = IP[:]
                    
                    if level == 0 :
                        START = len(IP_tmp)
                    else :
                        START = len(IP_tmp) - level + 1
                    
                    if l == 1 :
                        if L-START - 1 >= (3-level) and L-START - 1 <= 3 * (3-level) :
                            if level == 0 :
                                IP_tmp += s[START]
                            else :
                                IP_tmp += '.' + s[START]
                            out.append(IP_tmp)
                    
                    elif l == 2 :
                        if L-START - 2 >= (3-level) and L-START - 2 <= 3 * (3-level) :
                            if s[START] != '0' :
                                
                                if level == 0 :
                                    IP_tmp += s[START:START+2]
                                else :
                                    IP_tmp += '.' + s[START:START+2]
                                out.append(IP_tmp)
                                
                    elif l == 3 :
                        if L-START - 3 >= (3-level) and L-START - 3 <= 3 * (3-level) :
                            if s[START] == '1' :
                                if level == 0 :
                                    IP_tmp += s[START:START+3]
                                else :
                                    IP_tmp += '.' + s[START:START+3]
                                out.append(IP_tmp)
                            
                            elif s[START] == '2' :
                                if s[START + 1] >= '0' and s[START + 1] <= '4' :
                                    if level == 0 :
                                        IP_tmp += s[START:START+3]
                                    else :
                                        IP_tmp += '.' + s[START:START+3]
                                    out.append(IP_tmp)
                                    
                                elif s[START + 1] == '5' :
                                    if s[START + 2] >= '0' and s[START + 2] <= '5' :
                                        if level == 0 :
                                            IP_tmp += s[START:START+3]
                                        else :
                                            IP_tmp += '.' + s[START:START+3]
                                        out.append(IP_tmp)

        return out
        
        
        
        
        
        