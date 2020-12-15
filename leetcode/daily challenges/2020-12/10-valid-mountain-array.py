class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i = 1
        # check increasing
        while i < len(arr) - 1:
            if arr[i - 1] >= arr[i]:
                break
                
            i += 1
            
        # if we break first loop at first iteration, there is not increasing
        if i == 1:
            return False
          
        # check decreasing
        while i < len(arr):
            if arr[i - 1] <= arr[i]:
                break
                
            i += 1
            
        # must reach the end during decreasing for a valid mountain
        return i == len(arr)