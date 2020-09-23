class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        i = 0
        j = 1
        val = nums[0] 
        while val == 0 and i < len(nums) - 1:
            i += 1
            j += 1
            val = nums[i]
        if val == 0:
            return 0
        elif val > 0:
            m = 1
        else:
            m = 0
        
        while j < len(nums):
            if nums[j] != 0:
                val *= 1 if nums[j] > 0 else -1
                if val > 0:
                    m = max(m, 1 + j - i)
                j += 1
            else:
                while i < j - 1:
                    val *= 1 if nums[i] > 0 else -1
                    i += 1
                    if val > 0:
                        m = max(m, j - i)
                
                i = j + 1
                j = i + 1
                if i < len(nums):
                    val = nums[i]
                else:
                    return m
                
                while val == 0 and i < len(nums) - 1:
                    i += 1
                    j += 1
                    val = nums[i]
                if val == 0:
                    return m

        while i < j - 1:
            val /= nums[i]
            i += 1
            if val > 0:
                m = max(m, j - i)
                
        return m