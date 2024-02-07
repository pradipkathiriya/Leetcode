class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        min_heap = [[grid[0][0], 0, 0]]
        visit = set()
        visit.add((0, 0))
        while min_heap:
            max_elevation, x_cord, y_cord = heapq.heappop(min_heap)
            
            if x_cord == row - 1 and y_cord == col - 1:
                return max_elevation

            for dx, dy in directions:
                new_x_cord, new_y_cord = x_cord + dx, y_cord + dy
                if new_x_cord < 0 or new_x_cord == row or new_y_cord < 0 or new_y_cord == col:
                    continue
                if (new_x_cord, new_y_cord) in visit:
                    continue
                visit.add((new_x_cord, new_y_cord))
                new_max_elevation = max(max_elevation, grid[new_x_cord][new_y_cord])
                heapq.heappush(min_heap, [new_max_elevation, new_x_cord, new_y_cord])

        
        
