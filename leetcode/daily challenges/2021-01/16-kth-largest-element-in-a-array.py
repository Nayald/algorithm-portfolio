class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:        
        l = [nums[0]]
        for n in nums[1:]:
            if n >= l[-1]:
                l.append(n)
                
        return l[-k]