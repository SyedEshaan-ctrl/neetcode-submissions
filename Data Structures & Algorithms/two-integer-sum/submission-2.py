class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)): 
            s = target - nums[i]
            if s in nums[i+1:]:
                return [i , nums.index(s, i+1)]