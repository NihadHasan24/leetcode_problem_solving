class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # First pass: Cyclic sort
        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        
        # Second pass: Collect missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)
        return result
