class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        adj = collections.defaultdict(list)
        for src, dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)
        res = 0
        def dfs(node, prev_node):
            nonlocal res
            passanger = 0
            for child in adj[node]:
                if child == prev_node:
                    continue
                p = dfs(child, node)
                passanger += p
                res += int(ceil(p/seats))

            return passanger + 1

        passanger = dfs(0, -1)
        return res