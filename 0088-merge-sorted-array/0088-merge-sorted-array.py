class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n -1
        while i >=0 and j >=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while i>=0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1            
        while j>=0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1    
        return nums1    
        # i = 0
        # j = 0
        # count = 0
        # while (i < m and j < n):
        #     if nums1[i] <= nums2[j]:
        #         nums1[count] = nums1[i]
        #         count += 1
        #         i += 1
        #     else: 
        #         nums1[count] = nums2[j]
        #         count += 1
        #         j += 1
        # while i < m:
        #     nums1[count] = nums1[i]
        #     count += 1
        #     i += 1       
        # while j < n:
        #     nums1[count] = nums2[j]
        #     count += 1
        #     j += 1          
        # return nums1        

        