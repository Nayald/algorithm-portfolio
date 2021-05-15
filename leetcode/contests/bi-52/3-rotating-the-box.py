class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in range(len(box)):
            l = [0]
            for j in range(len(box[0])):
                if box[i][j] == "#":
                    l[-1] += 1
                    box[i][j] = "."
                elif box[i][j] == "*":
                    l.append(0)
                    
            for j in reversed(range(len(box[0]))):
                if l[-1]:
                    box[i][j] = "#"
                    l[-1] -= 1
                
                if box[i][j] == "*":
                    l.pop()
        
        #print(*list(zip(*box[::-1])), sep="\n")
        return list(zip(*box[::-1]))