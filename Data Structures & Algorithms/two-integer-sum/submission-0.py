class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key = {}
        for i in range(len(nums)):
            if nums[i] in key:
                return [key[nums[i]], i]
            else:
                key[target - nums[i]] = i
        