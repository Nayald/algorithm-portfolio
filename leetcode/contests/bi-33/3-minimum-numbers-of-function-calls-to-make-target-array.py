class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        while any(n > 0 for n in nums):
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    op += 1
                nums[i] >>= 1
            op += 1
        
        return op - 1