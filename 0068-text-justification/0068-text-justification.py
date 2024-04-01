class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        result = []
        tmp_str = ""
        tmp_list = []
        
        for w in words :
            
            #print(w, result, tmp_str, tmp_list)

            if len(tmp_str) == 0:
                tmp_str += w
                tmp_list.append(w)
                
            else :
                if len(tmp_str) + 1 + len(w) <= maxWidth :
                    tmp_str += (" " + w)
                    tmp_list.append(w)
                else :
                    if len(tmp_list) == 1 :
                        tmp_str = tmp_list[0] + " " * (maxWidth - len(tmp_list[0]))
                        result.append(tmp_str)
                        tmp_str = ""
                        tmp_list = []
                    else :
                        N = maxWidth - len(tmp_str)
                        if N == 0:
                            result.append(tmp_str)
                            tmp_str = ""
                            tmp_list = []
                        else :
                            num_space = len(tmp_list) - 1
                            q = N // num_space
                            r = N % num_space
                            tmp_str = tmp_list[0]
                            for i in range(1, len(tmp_list)):
                                if i<= r:
                                    tmp_str += (" "*(q+2) + tmp_list[i])
                                else :
                                    tmp_str += (" "*(q+1) + tmp_list[i])
                            result.append(tmp_str)
                            tmp_str = ""
                            tmp_list = []
                    tmp_str += w
                    tmp_list.append(w)
        


        tmp_str += " " * (maxWidth - len(tmp_str))
        result.append(tmp_str)
        tmp_str = ""
        tmp_list = []
        
        
        return result
    






