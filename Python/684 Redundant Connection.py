class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        union_find = UnionFind(edges)
        for e1, e2 in edges:
            par1 = union_find.find(e1)
            par2 = union_find.find(e2)
            if par1 == par2:
                return [e1, e2]
            union_find.union(par1, par2)

class UnionFind():
    def __init__(self, edges):
        n = len(edges)
        self.par = [i for i in range(n + 1)]
        self.rank = [1 for i in range(n+1)]

    def find(self, node):
        p = self.par[node]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, par1, par2):
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += 1
        else:
            self.par[par1] = par2
            self.rank[par2] += 1