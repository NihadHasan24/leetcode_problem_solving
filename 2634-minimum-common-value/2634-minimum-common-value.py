class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        while (i <len(nums1) and j<len(nums2)):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]: 
                i += 1
            else:
                j += 1
        return -1             
        

        # Brute force
        # for i in nums1:
        #     for j in nums2: 
        #        if i == j:
        #           return i
        # return -1

        