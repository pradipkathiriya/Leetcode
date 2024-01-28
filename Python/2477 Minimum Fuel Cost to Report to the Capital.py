class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        adj = collections.defaultdict(list)
        for src, dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node, prev_node):
            passanger = 0
            res = 0
            for child in adj[node]:
                if child == prev_node:
                    continue
                p, r = dfs(child, node)
                passanger += p
                res += int(p/seats)
                res += (p%seats > 0)
                res += r

            return (passanger + 1, res)

        passanger, res = dfs(0, -1)
        return res