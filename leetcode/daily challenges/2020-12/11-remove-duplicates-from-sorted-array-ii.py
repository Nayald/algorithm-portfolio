class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        
        k = 0
        i = 0
        j = 1
        while i + k < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
                
            if j > i + 2:
                i += 2
                for m in reversed(range(i, j)):
                    while m < len(nums) - k - 1:
                        nums[m], nums[m+1] = nums[m+1], nums[m]
                        m += 1
                        
                    k += 1
                
                j = i + 1
            else:
                i = j
                
        return len(nums) - k