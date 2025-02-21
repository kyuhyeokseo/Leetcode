class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        # Case 1 : IPv4
        v4_list = queryIP.split('.')
        v4_flag = True
        if len(v4_list) == 4 :
            for item in v4_list :
                if not item.isdecimal():
                    v4_flag = False
                    break
                if int(item) > 255 or int(item) < 0 :
                    v4_flag = False
                    break
                if int(item) == 0 and len(item) > 1 :
                    v4_flag = False
                    break
                if int(item) != 0 and item[0] == '0' :
                    v4_flag = False
                    break
            if v4_flag :
                return 'IPv4'
        
        # Case 2 : IPv6
        v6_list = queryIP.split(':')
        v6_flag = True

        if len(v6_list) == 8 :
            for item in v6_list :
                if len(item) < 1 or len(item) > 4 :
                    v6_flag = False
                    break

                for x in item :
                    if not( (ord(x)>=ord('0') and ord(x)<=ord('9')) or (ord(x)>=ord('a') and ord(x)<=ord('f')) or (ord(x)>=ord('A') and ord(x)<=ord('F'))):
                        v6_flag = False
                if v6_flag == False :
                    break
                
            if v6_flag :
                return 'IPv6'
        
        # Case 3
        return 'Neither'