class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row , col = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i,j):
            if i < 0 or j < 0 or i == row or j == row or (i,j) in visited or grid[i][j] == 0:
                return 
            visited.add((i, j))
            q.append([i, j])
            for dx, dy in direction:
                x, y = i + dx, j + dy
                dfs(x, y)

        def bfs():
            result = 0
            while q:
                length = len(q)
                for i in range(length):
                    x, y = q.popleft()
                    for dx, dy in direction:
                        i, j = x + dx, y + dy
                        if i < 0 or j < 0 or i == row or j == row or (i,j) in visited:
                            continue
                        if grid[i][j] == 1:
                            return result
                        
                        visited.add((i, j))
                        q.append([i, j])
                result += 1

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    dfs(i, j)
                    return bfs()
        