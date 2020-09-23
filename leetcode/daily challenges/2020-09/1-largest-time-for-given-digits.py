from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        biggest = ""
        for i in permutations(A):
            candidate = "".join(map(str, i))
            candidate = "0" if len(candidate) == 3 else "" + candidate
            if valid_time(candidate):
                biggest = max(biggest, candidate)
                
        return (biggest[:2] + ":" + biggest[2:]) if biggest != "" else ""
            
            
            
def valid_time(t):
    return (t[0] in set(map(str, range(0, 3)))) and (t[1] in (set(map(str, range(0, 10))) if t[0] < "2" else set(map(str, range(0, 4))))) and (t[2] in set(map(str, range(0, 6)))) and (t[3] in set(map(str, range(0, 10))))