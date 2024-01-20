class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_length, col_length = len(grid), len(grid[0])

        q = collections.deque()
        q.append([0, 0])
        visited = set((0, 0))
        direction = [[1,0], [0,1], [-1,0], [0,-1],
                     [1,1], [1,-1], [-1,1], [-1,-1]]
        if row_length == col_length == 1:
            if grid[0][0] == 0:
                return 1
        if grid[0][0] == 1:
            return -1

        result = 0
        while q:
            length = len(q)
            result += 1
            for i in range(length):
                x, y = q.popleft()
                for dx, dy in direction:
                    row, col = x + dx, y + dy
                    if row < 0 or col < 0 or row == row_length or col == col_length or grid[row][col] == 1 or (row, col) in visited:
                        continue
                    
                    if row == row_length - 1 and col == col_length - 1:
                        result += 1
                        return result
                    visited.add((row, col))
                    q.append([row, col])

        return -1