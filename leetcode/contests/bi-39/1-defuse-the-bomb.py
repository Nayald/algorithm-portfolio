class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            code2 = []
            for i in range(len(code)):
                val = 0
                for j in range(1,k+1):
                    val += code[(i+j)%len(code)]

                code2.append(val)

            return code2
        else:
            code2 = []
            for i in range(len(code)):
                val = 0
                for j in range(1,abs(k)+1):
                    val += code[(i-j)%len(code)]

                code2.append(val)

            return code2