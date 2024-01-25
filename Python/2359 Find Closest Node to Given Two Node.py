class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        def bfs(node):
            node_dist= {}
            q = collections.deque()
            q.append([node, 0])
            node_dist[node] = 0
            while q:
                node, dist = q.popleft()
                if edges[node] != -1 and edges[node] not in node_dist:
                    new_node = edges[node]
                    q.append([new_node, dist + 1])
                    node_dist[new_node] = dist + 1
            return node_dist

        node_1_dist = bfs(node1)
        node_2_dist = bfs(node2)

        res = -1
        max_dist = float("inf")
        for i in range(len(edges)):
            if i in node_1_dist and i in node_2_dist:
                dist = max(node_1_dist[i], node_2_dist[i])
                if dist < max_dist:
                    max_dist = dist
                    res = i

        return res