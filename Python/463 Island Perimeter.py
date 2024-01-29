# class Solution(object):
#     def islandPerimeter(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """

#         row, col = len(grid), len(grid[0])

#         q = collections.deque()

#         per = 0

#         visited  = set()

#         for i in range(row):
#              for j in range(col):
#                 if grid[i][j] == 1:
#                     q.append((i,j))
#                     visited.add((i,j))

#                     while q:

#                         a, b = q.popleft()
#                         n = 4

#                         if a -1 >= 0 and (a-1,b) not in visited and grid[a-1][b] == 1:
#                             n -= 1
#                             q.append((a-1,b))
#                             visited.add((a-1,b))

#                         if a +1 < row and (a+1,b) not in visited and grid[a+1][b] == 1:
#                             n -= 1
#                             q.append((a+1,b))
#                             visited.add((a+1,b))

#                         if b-1 >= 0 and (a,b-1) not in visited and grid[a][b-1] == 1:
#                             n -= 1
#                             q.append((a,b-1))
#                             visited.add((a,b-1))

#                         if b + 1 < col and (a,b+1) not in visited and grid[a][b+1] == 1:
#                             n -= 1
#                             q.append((a,b+1))
#                             visited.add((a,b+1))

#                         per += n

#                     break

#         return per

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        per = 0
        visited = set()
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    q = collections.deque([(i,j)])
                    visited.add((i,j))

                    while q:
                        a, b = q.popleft()
                        n = 4

                        if a-1 >= 0 and grid[a-1][b] == 1:
                            n -= 1
                            if (a-1,b) not in visited:
                                q.append((a-1,b))
                                visited.add((a-1,b))

                        if a+1 < row and grid[a+1][b] == 1:
                            if (a+1,b) not in visited:
                                q.append((a+1,b))
                                visited.add((a+1,b))
                            n -= 1
                        
                        if b-1 >= 0 and grid[a][b-1] == 1:
                            if (a,b-1) not in visited:
                                q.append((a,b-1))
                                visited.add((a,b-1))
                            n -= 1
                            
                        if b+1 < col and grid[a][b+1] == 1:
                            if (a,b+1) not in visited:
                                q.append((a,b+1))
                                visited.add((a,b+1))
                            n -= 1
                            
                        per +=n

                    return per



                