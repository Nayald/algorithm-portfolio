class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        sub = 1
        while memory1 >= 0 and memory2 >= 0:
            if memory1 >= memory2:
                memory1 -= sub
            else:
                memory2 -= sub
                
            sub += 1
            
        if memory1 < 0:
            sub -= 1
            memory1 += sub
        elif memory2 < 0:
            sub -= 1
            memory2 += sub
            
        return [sub, memory1, memory2]