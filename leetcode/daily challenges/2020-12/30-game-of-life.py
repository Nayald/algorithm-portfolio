class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        next = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                for k in (i-1, i, i+1):
                    if 0 <= k < len(board):
                        for l in (j-1, j, j+1):
                            if 0 <= l < len(board[0]) and (k != i or l != j):
                                next[i][j] += board[k][l]
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1 and (next[i][j] < 2 or next[i][j] > 3):
                    board[i][j] = 0
                elif board[i][j] == 0 and next[i][j] == 3:
                    board[i][j] = 1

        