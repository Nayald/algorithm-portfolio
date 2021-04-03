from functools import lru_cache

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            rev1 = rev(num)
            if num - rev1 not in d:
                d[num - rev1] = 1
            else:
                d[num - rev1] += 1
        
        #print(d)
        result = 0
        for k in d:
            result += int(fact(d[k]) / (fact(2) * fact(d[k] - 2)))
            
        return result % (10 ** 9 + 7)

        #result = 0
        #for i in range(len(nums)):
        #    for j in range(i + 1, len(nums)):
        #        rev1 = rev(nums[i])
        #        rev2 = rev(nums[j])
        #        if nums[i] + rev2 == rev1 + nums[j]:
        #            result += 1
        #        
        #return result
    
                
def rev(num):
    return int(str(num)[::-1])


@lru_cache
def fact(n):
    if n <= 1:
        return 1
    
    return n * fact(n - 1)