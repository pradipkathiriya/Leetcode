class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        visited = set()
        result = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i == row or j == col:
                return False 

            if grid[i][j] == 1 or (i, j) in visited:
                return True
            visited.add((i, j))

            res = dfs(i + 1, j)
            res = dfs(i - 1, j) and res
            res = dfs(i, j + 1) and res
            res = dfs(i, j - 1) and res

            return res

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 and (i, j) not in visited:
                    result += dfs(i, j)

        return result