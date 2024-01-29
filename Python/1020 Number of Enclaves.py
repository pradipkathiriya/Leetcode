class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        visited = set()
        result = 0

        def dfs(i ,j):
            if i < 0 or j < 0 or i == row or j == col or grid[i][j] == 0 or (i, j) in visited:
                return 
            visited.add((i ,j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(row):
            if grid[i][0] == 1 and (i, 0) not in visited:
                dfs(i, 0)
            if grid[i][col - 1] and (i, col - 1) not in visited:
                dfs(i, col - 1)

        for j in range(col):
            if grid[0][j] == 1 and (0, j) not in visited:
                dfs(0, j)
            if grid[row - 1][j] == 1 and (row - 1, j) not in visited:
                dfs(row - 1, j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i ,j) not in visited:
                    result += 1
        return result