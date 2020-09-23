class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = n2 = -1
        c1 = c2 = 0
                       
        for e in nums:
            if n1 == e:
                c1 += 1
            elif n2 == e:
                c2 += 1
            elif c1 == 0:
                n1 = e
                c1 = 1
            elif c2 == 0:
                n2 = e
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        
        c1 = c2 = 0
        for e in nums:
            if e == n1:
                c1 += 1
            elif e == n2:
                c2 += 1
                
        r = []
        if c1 > len(nums) // 3:
            r.append(n1)
        if c2 > len(nums) // 3:
            r.append(n2)
            
        return r
        