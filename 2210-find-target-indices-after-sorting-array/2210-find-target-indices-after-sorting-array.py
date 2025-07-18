class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less=0
        equal=0
        for elem in nums:
            if elem<target:
                less+=1
            elif elem==target:
                equal+=1
        return [j for j in range(less,less+equal)]
        # res = []
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res.append(i)
        # return res        
        