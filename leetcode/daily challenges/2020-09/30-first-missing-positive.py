class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                continue
            i += 1
        
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
            
        return len(nums) + 1
                
        