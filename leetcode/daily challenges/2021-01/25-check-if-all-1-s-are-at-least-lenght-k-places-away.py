class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = k
        for n in nums:
            if n == 1:
                if dist < k:
                    return False
                else:
                    dist = 0
            else:
                dist += 1
                
        return True
            