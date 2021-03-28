class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove.append(i)
                    
        result = []
        i = 0
        for j in gen(stack, to_remove):
            result.append(s[i:j])
            i = j + 1
            
        result.append(s[i:])
        return "".join(result)
    
def gen(l1, l2):
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            yield l1[i]
            i += 1
        else:
            yield l2[j]
            j += 1
            
    yield from l1[i:] or l2[j:]