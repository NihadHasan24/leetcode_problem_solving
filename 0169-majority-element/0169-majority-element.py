class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moore's voting algo (optimal)
        count = 0 
        elem = 0
        for i in range(len(nums)):
            if count == 0:
                count = 1
                elem = nums[i]
            elif nums[i] == elem:
                count += 1
            else:
                count -= 1
        count1 = 0        
        for i in range(len(nums)):
            if nums[i] == elem:
                count1 += 1
        if count1>(len(nums)//2):
            return elem   
                              
        #better solution
        # dic = {}
        # for i in range(len(nums)):
        #     if nums[i] not in dic:
        #         dic[nums[i]] = 1
        #     else:
        #         dic[nums[i]]  += 1     
        # for val in dic:
        #     if dic[val]>(len(nums)//2):
        #         return val  

        # Brute Force
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        #     if count > (len(nums) //2):
        #         return nums[i]
