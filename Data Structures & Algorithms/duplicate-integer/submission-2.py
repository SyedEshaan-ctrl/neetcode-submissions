class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for i in range(0,len(nums)):
            if nums[i] in unique: 
                return True 
            else : 
                unique.add(nums[i])
        return False 