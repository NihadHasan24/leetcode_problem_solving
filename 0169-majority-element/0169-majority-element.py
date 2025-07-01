class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #better solution
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]]  += 1     
        for val in dic:
            if dic[val]>(len(nums)//2):
                return val            
        # Brute Force
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        #     if count > (len(nums) //2):
        #         return nums[i]
