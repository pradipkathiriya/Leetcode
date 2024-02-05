class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        adj = collections.defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([weight, j])
                adj[j].append([weight, i])

        min_cost = 0
        visit = set()
        min_heap = [[0, 0]]

        while min_heap:
            weight, i = heapq.heappop(min_heap)
            if i in visit:
                continue
            visit.add(i)
            min_cost += weight
            if len(visit) == len(points):
                return min_cost
            for new_weight, j in adj[i]:
                heapq.heappush(min_heap, [new_weight, j])
