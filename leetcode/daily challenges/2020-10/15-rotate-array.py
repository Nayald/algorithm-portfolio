class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = k % len(nums)
        if shift == 0:
            return
        
        start = 0
        for _ in range(pgcd(shift, len(nums))):
            tmp = nums[start]
            current = (start + shift) % len(nums)
            while current != start:
                nums[current], tmp = tmp, nums[current]
                current = (current + shift) % len(nums)
                
            nums[start] = tmp
            start += 1
            
            
def pgcd(a, b):
    while b != 0:
        a , b = b , a % b
        
    return a