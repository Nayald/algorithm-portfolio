class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        r = [nums]
        s = {tuple(nums)}
        for i in range(len(nums) - 1):
            for j in range(len(r)):
                frozen = r[j][:i]
                rollable = r[j][i:]
                for k in range(1, len(rollable)):
                    c = frozen + rollable[-k:] + rollable[:-k]
                    if tuple(c) not in s:
                        s.add(tuple(c))
                        r.append(c)
                    
        return r