class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        ret = []
        D = {}

        for path in paths:
            files = list(path.split(' '))
            direc = files[0]

            for f in files[1:]:
                srt, end = f.find('('), -1

                file_name = f[:srt]
                content = f[srt+1:end]

                if content in D:
                    D[content].append(direc + '/' + file_name)
                else :
                    D[content] = [direc + '/' + file_name]
        
        for k in D.keys():
            if len(D[k]) > 1:
                ret.append(D[k][:])

        return ret