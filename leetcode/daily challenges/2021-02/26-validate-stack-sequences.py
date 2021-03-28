class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = j = 0
        while i < len(pushed):
            #print(stack, i, j)
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                stack.append(pushed[i])
                i += 1
                
        while stack:
            #print(stack, i, j)
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                return False
            
        return True