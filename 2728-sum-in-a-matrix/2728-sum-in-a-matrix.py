class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()

        score = 0
        for c in zip(*nums):
            score += max(c)
        
        return score
        # row,col = len(nums),len(nums[0])
        # score = 0
        # for i in range(col):
        #     maxi = float(-inf)
        #     for j in range(row):
        #         if nums[j][i]>maxi:
        #             maxi = nums[j][i]
        #     score += maxi
        # return score            
        