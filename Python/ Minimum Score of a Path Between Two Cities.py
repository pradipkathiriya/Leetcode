class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))
        visited = set()
        
        def dfs(i):
            res = float("inf")
            for child, dst in adj[i]:
                if (child, i) in visited or (i, child) in visited:
                    continue
                visited.add((child,i))
                curr_res = dfs(child)
                res = min(res, dst, curr_res)
            return res
        return dfs(1)