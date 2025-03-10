class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ret = []

        if len(nums) == 1:
            return ret
        
        for j in range(1, len(nums)):

            new = nums[j]
            tmp = []

            if ret :
                for item in ret:
                    tmp.append(item)
                    if item[-1] <= new:
                        newitem = item + (new, )
                        tmp.append(newitem)

            for i in range(j):
                if nums[i] <= new:
                    newitem = (nums[i], new)
                    tmp.append(newitem)

            ret = list(set(tmp))
            #print(ret)
        
        out = []
        for x in ret :
            out.append(list(x))
        return out


