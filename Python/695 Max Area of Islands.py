class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        visited = [[0 for j in range(col)] for i in range(row)]

        que = collections.deque()

        result = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = 0
                    que.append([i,j])
                    visited[i][j] = 1
                    while que:
                        a, b = que.popleft()
                        area += 1
                        neighbours = [[a-1,b],[a+1,b],[a, b-1],[a,b+1]]

                        for x, y in neighbours:
                            if x in range(row) and y in range(col) and grid[x][y] == 1 and not visited[x][y]:
                                que.append([x,y])
                                visited[x][y] = 1

                    result = max(area, result)

        return result