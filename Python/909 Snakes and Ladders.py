class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        length = len(board)
        def square_to_index(square):
            r = (square - 1) // length
            r = length - r - 1
            c = (square - 1) % length
            if length % 2 == r % 2:
                c = length - c - 1
            # if length % 2:
            #     if r % 2:
            #         c = length - c - 1
            # if length % 2 == 0:
            #     if r % 2 == 0:
            #         c = length - c - 1
            return [r ,c]

        q = collections.deque()
        q.append([1, 0]) # square, moves
        visited = set()

        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                next_square = square + i
                r, c = square_to_index(next_square)
                
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == length * length :
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    q.append([next_square, moves + 1])
                print('r')
                print(r)
                print('c')
                print(c)
                print('nxtsqr')
                print(next_square)

        return -1
      