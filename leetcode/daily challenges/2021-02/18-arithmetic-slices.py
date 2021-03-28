class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        diff = [A[i+1] - A[i] for i in range(len(A) - 1)]
        result = 0
        i = 0
        j = 0
        size = 0
        while j < len(diff):
            if diff[i] != diff[j]:
                i = j
                
            if j - i + 1 >= 2:
                size += 1
            else:
                result += size*(size+1)//2
                size = 0
                
            j += 1
            
        return result + size*(size+1)//2
                
            
                