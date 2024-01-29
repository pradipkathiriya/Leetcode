class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """

        row , col = len(grid2), len(grid2[0])

        q = collections.deque()

        visited = set()

        result = 0

        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    q.append((i,j))
                    visited.add((i,j))

                    isSub = True

                    while q:

                        a, b = q.popleft()

                        if grid1[a][b] == 0:
                            isSub = False

                        if a - 1 >= 0 and grid2[a-1][b] == 1 and (a-1,b) not in visited:
                            q.append((a-1,b))
                            visited.add((a-1,b))

                        if a + 1 < row and grid2[a+1][b] == 1 and (a+1,b) not in visited:
                            q.append((a+1,b))
                            visited.add((a+1,b))

                        if b - 1 >= 0 and grid2[a][b-1] == 1 and (a,b-1) not in visited:
                            q.append((a,b-1))
                            visited.add((a,b-1))

                        if b + 1 < col and grid2[a][b+1] == 1 and (a,b+1) not in visited:
                            q.append((a,b+1))
                            visited.add((a,b+1))

                    if isSub:
                        result += 1


        return result




                        

