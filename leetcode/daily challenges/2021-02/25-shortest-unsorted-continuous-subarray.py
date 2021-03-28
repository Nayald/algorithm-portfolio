class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                break
        else:
            return 0
        
        for j in reversed(range(1, len(nums))):
            if nums[j] < nums[j-1]:
                break
                
        min_val = min(nums[i:j+1])
        max_val = max(nums[i:j+1])        
        while i >= 0 and nums[i] > min_val:
            i -= 1
            
        while j < len(nums) and nums[j] < max_val:
            j += 1
            
        return j - (i + 1)