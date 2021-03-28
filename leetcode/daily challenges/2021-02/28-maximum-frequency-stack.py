class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stacks = {}
        self.max = 0

    def push(self, x: int) -> None:
        if x not in self.freq:
            self.freq[x] = 1
        else:
            self.freq[x] += 1
            
        freq = self.freq[x]
        if freq not in self.stacks:
            self.stacks[freq] = [x]
        else:
            self.stacks[freq].append(x)
            
        self.max = max(self.max, freq)

    def pop(self) -> int:     
        val = self.stacks[self.max].pop()
        self.freq[val] -= 1
        if not self.stacks[self.max]:
            self.max -= 1
        
        return val
    
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()