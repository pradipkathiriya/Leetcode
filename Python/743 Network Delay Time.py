class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        adj = collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append([v, w])

        min_heap = [[0, k]]
        visit = set()

        while min_heap:
            curr_weight, curr_node = heapq.heappop(min_heap)
            if curr_node in visit:
                continue
            visit.add(curr_node)
            if len(visit) == n:
                return curr_weight
            for child, edge_weight in adj[curr_node]:
                heapq.heappush(min_heap, [curr_weight + edge_weight, child])
        
        return -1