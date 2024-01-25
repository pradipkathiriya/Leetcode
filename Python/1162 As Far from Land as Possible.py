class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row, col = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        def out_of_bound(i, j):
            if (i < 0 or j < 0 or i == row or j == col):
                return True
            return False
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    q.append([i, j, 0])

        if len(q) == row * col or len(q) == 0:
            return -1
        res = -1
        direction = [[1, 0], [-1 , 0], [0, 1], [0, -1]]
    
        while q:
            length = len(q)
            for i in range(length):
                x, y, dist = q.popleft()
                for dx, dy in direction:
                    new_x = x + dx
                    new_y = y + dy
                    if not out_of_bound(new_x, new_y) and (new_x, new_y) not in visited:
                        q.append([new_x, new_y, dist + 1])
                        visited.add((new_x, new_y))
                        print(new_x, new_y, dist + 1)
                        res = max(res, dist + 1)

        return res


      