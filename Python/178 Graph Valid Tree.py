class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n, edges):
        # write your code here
        if n == 0:
            return True
        neighbour = {i : [] for i in range(n)}
        for e1, e2 in edges:
            neighbour[e1].append(e2)
            neighbour[e2].append(e1)
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False
            visited.add(i)
            for nei in neighbour:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False

            return True

        if dfs(0, -1) and len(visited) == n:
            return True
        else:
            return False