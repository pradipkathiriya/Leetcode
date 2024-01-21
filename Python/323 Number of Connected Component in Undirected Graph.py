class Solution:
    def count_components(self, n, edges):
        result = n
        union_find = UnionFind()
        for e1, e2 in edges:
            result -= union_find.find(e1, e2)
        return result
        
class UnionFind():
    def __init__(self, n, edges):
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
    def find(self, node):
        p = self.par[node]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
            
        return p
    def union(self, e1, e2):
        par1 = self.par[e1]
        par2 = self.par[e2]
        
        if par1 == par2:
            return 0
        
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
            self.rank[par1] += 1
        else:
            self.par[par1] = par2
            self.rank[par2] = par1   
        
        return 1
    
if __name__ == '__main__':
    print('hello')
        