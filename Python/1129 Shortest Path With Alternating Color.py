class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        red_edges = collections.defaultdict(list)
        blue_edges = collections.defaultdict(list)

        for start, dst in redEdges:
            red_edges[start].append(dst)

        for start , dst in blueEdges:
            blue_edges[start].append(dst)

        answer = [-1 for i in range(n)]

        q = collections.deque()
        q.append([0, 0, None])
        visit = set()
        visit.add((0, None))

        while q:
            node, length, color = q.popleft()
            if answer[node] == -1:
                answer[node] = length

            if color != "RED":
                for nei in red_edges[node]:
                    if (nei, "RED") not in visit:
                        visit.add((nei, "RED"))
                        q.append([nei, length + 1, "RED"])

            if color != "BLUE":
                for nei in blue_edges[node]:
                    if (nei, "BLUE") not in visit:
                        visit.add((nei, "BLUE"))
                        q.append([nei, length + 1, "BLUE"])

        return answer
        