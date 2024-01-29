class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        row, col = len(grid), len(grid[0])
        num_island = 0
        visited = [[0 for j in range(col)] for i in range(row)]
        prio_que = collections.deque()


        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and not visited[i][j]:
                    num_island += 1
                    prio_que.append((i,j))
                    visited[i][j] = 1
                    while prio_que:
                        a, b = prio_que.popleft()
                        
                        neighbours = [[a-1,b],[a+1,b],[a,b-1],[a,b+1]]

                        for p, q in neighbours:
                            if p in range(row) and q in range(col) and grid[p][q] == '1' and not visited[p][q]:
                                visited[p][q] = 1
                                prio_que.append((p,q))

        
        return num_island






        