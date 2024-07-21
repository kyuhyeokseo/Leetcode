MAX = 2**20

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        if len(nums1) > len(nums2) :
            return self.findMedianSortedArrays(nums2, nums1)
        
        
        L_tot = (len(nums1) + len(nums2) + 1) // 2
        is_odd = (len(nums1) + len(nums2)) % 2
        
        start = 0
        end = len(nums1)
        
        while (start <= end) :
            curr1 = (start + end)//2
            curr2 = L_tot - curr1
            
            max1 = nums1[curr1-1] if curr1 > 0 else -MAX
            min1 = nums1[curr1] if curr1 < len(nums1) else MAX
        
            max2 = nums2[curr2-1] if curr2 > 0 else -MAX
            min2 = nums2[curr2] if curr2 < len(nums2) else MAX
            
            if max1 <= min2 and max2 <= min1 :
                if is_odd :
                    return max(max1, max2)
                else :
                    return (max(max1, max2) + min(min1, min2))/2
            elif max1 > min2 :
                end = curr1 - 1
            else :
                start = curr1 + 1