class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(t=0, j=0, path=[]):
            if t == target:
                result.append(path)
                return
            if t > target:
                return
            
            while j < len(candidates):
                tt = t + candidates[j]
                backtrack(tt, j, path + [candidates[j]])
                j += 1
                
        backtrack()
        return result