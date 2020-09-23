class Solution:
    def __init__(self):
        self.ops = {"G" : self.walk, "L": self.turnLeft, "R": self.turnRight}
    
    def isRobotBounded(self, instructions: str) -> bool:
        self.vec = (0, 1)
        self.pos = [0, 0]
        
        for op in instructions:
            self.ops[op]()
        return self.pos == [0, 0] or self.vec != (0, 1)
            

    def walk(self):
        self.pos[0] += self.vec[0]
        self.pos[1] += self.vec[1]
            
    def turnLeft(self):
        self.vec = (self.vec[1], -self.vec[0])

    def turnRight(self):
        self.vec = (-self.vec[1], self.vec[0])