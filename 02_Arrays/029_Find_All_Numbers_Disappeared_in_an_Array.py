class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        return [i + 1 for i, val in enumerate(nums) if val > 0]
