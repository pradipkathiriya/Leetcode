class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        adj = collections.defaultdict(list)

        #{node: [neighbor, max_prob]}
        for i in range(len(edges)):
            node_1, node_2  = edges[i]
            probability = succProb[i]
            adj[node_1].append([node_2, probability]) 
            adj[node_2].append([node_1, probability]) 
        print(adj)
        visit = set()
        min_heap = [[-1, start_node]]

        while min_heap:
            prob, curr_node = heapq.heappop(min_heap)
            prob *= -1
            if curr_node == end_node:
                return prob
            visit.add(curr_node)
            for next_node, p in adj[curr_node]:
                if next_node in visit:
                    continue
                heapq.heappush(min_heap, [-1 * p * prob, next_node])

        return 0