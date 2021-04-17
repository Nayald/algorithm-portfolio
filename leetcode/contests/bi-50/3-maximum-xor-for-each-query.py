class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
            
        result = []
        for i in reversed(range(len(nums))):
            k = xor ^ (2 ** maximumBit - 1)            
            result.append(k)
            xor ^= nums[i]
            
        return result