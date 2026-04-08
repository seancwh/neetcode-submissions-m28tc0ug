class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        conMap = {}
        for i in nums:
            if i in conMap:
                return True
            conMap[i] = i
        return False 

        