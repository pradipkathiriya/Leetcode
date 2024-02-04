class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        row, col = len(heights), len(heights[0])
        visit = set()
        min_heap = [[0, 0, 0]]
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while min_heap:
            curr_max_effort, r, c = heapq.heappop(min_heap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r == row - 1 and c == col - 1:
                return curr_max_effort

            for dx, dy in direction:
                x, y = r + dx, c - dy
                if x < 0 or y < 0 or x == row or y == col:
                    continue
                new_max_effort = max(curr_max_effort, abs(heights[x][y] - heights[r][c]))
                heapq.heappush(min_heap, [new_max_effort, x, y])