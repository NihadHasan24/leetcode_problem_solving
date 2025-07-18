from bisect import bisect_left,bisect_right
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # optimal
        neg = bisect_left(nums, 0)      # index of first 0 = count of negative numbers
        pos = len(nums) - bisect_right(nums, 0)  # elements strictly > 0
        return max(neg, pos)



        # Brute
        # positive_count = 0
        # negative_count = 0
        # for elem in nums:
        #     if elem > 0:
        #         positive_count += 1
        #     elif elem < 0:
        #         negative_count += 1
        # if positive_count >= negative_count:
        #     return (positive_count)
        # else:
        #     return (negative_count)                
        