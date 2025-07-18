class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive_count = 0
        negative_count = 0
        for elem in nums:
            if elem > 0:
                positive_count += 1
            elif elem < 0:
                negative_count += 1
        if positive_count >= negative_count:
            return (positive_count)
        else:
            return (negative_count)                
        