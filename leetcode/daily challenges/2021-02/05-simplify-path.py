class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for dir in path.split("/"):
            if dir not in {"", ".", ".."}:
                stack.append(dir)
            elif dir == ".." and stack:
                stack.pop()
                
        return "/" + "/".join(stack)