class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:       
        result = abs(nums[0])
        max_s = nums[0]
        min_s = nums[0]
        for i in range(1, len(nums)):
            abs_s = max(abs(nums[i]), abs(max_s + nums[i]), abs(min_s + nums[i]))
            max_s = max(nums[i], max_s + nums[i])
            min_s = min(nums[i], min_s + nums[i])
            result = max(result, abs_s)
            #print(nums[i], max_s, min_s, abs_s)
                
        return result