class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        """
        :type board: List[List[str]]
        :type rMove: int
        :type cMove: int
        :type color: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])

        moves = [[-1 , 0], [1, 0], [0, -1], [0, 1],
                  [1, -1], [1, 1], [-1, 1], [-1, -1]]

        def dfs(dx, dy, i, j, length):
            if i == row or j == col or i < 0 or j < 0:
                return False

            if board[i][j] == "." and length > 0:
                return False

            if board[i][j] == color:
                if length > 1:
                    return True
                else:
                    return False

            i = i + dx
            j = j + dy
            length = length + 1

            return dfs(dx, dy, i, j, length) 

        for dx, dy in moves:
            if dfs(dx, dy, rMove, cMove,  0):
                return True

        return False



        