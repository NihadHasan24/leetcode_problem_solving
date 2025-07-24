class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        count = 0
        while i < j:
            if nums[i] + nums[j] < target:
                count += j - i
                i += 1
            else:
                j -= 1
        return  count          

        
        # Brute force (n^2)
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if i != j:
        #            if nums[i] + nums[j] < target:
        #              count += 1
        # return count            
        