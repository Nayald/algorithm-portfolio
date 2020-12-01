class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        numbers = []
        ops = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
                
            if "0" <= s[i] <= "9":
                j = i + 1
                while j < len(s) and "0" <= s[j] <= "9":
                    j += 1
            
                numbers.append(int(s[i:j]))
                i = j
            elif s[i] in {"*", "/"}:
                k = i + 1
                while s[k] == " ":
                    k += 1
                    
                j = k + 1
                while j < len(s) and "0" <= s[j] <= "9":
                    j += 1
                
                a = numbers.pop()
                b = int(s[k:j])
                numbers.append((a * b) if s[i] == "*" else (a // b))
                i = j
            else:
                ops.append(s[i])
                i += 1
        
        result = numbers[0]
        for val, op in zip(numbers[1:], ops):
            if op == "+":
                result += val
            else:
                result -= val
            
        return result