class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 :
            for i in range(n):
                nums1[i] = nums2[i]

        elif len(nums2) != 0 :
            L = len(nums1)
            x = m-1
            i,j = 0, 0
            for l in range(L):
                if i == m:
                    x += 1
                    nums1[x] = nums2[j]
                    j += 1
                elif j == n :
                    tmp = nums1.pop(0)
                    nums1.append(tmp)
                    i += 1
                elif nums1[0] < nums2[j]:
                    tmp = nums1.pop(0)
                    nums1[x] = tmp
                    nums1.append(0)
                    i += 1
                else :
                    x += 1
                    nums1[x] = nums2[j]
                    j += 1
        