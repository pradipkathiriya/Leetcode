import collections
class UnionFind():
    def __init__(self, length):
        self.par = [i for i in range(length)]
        self.rank = [1] * length

    def find(self, node):
        p = self.par[node]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_acc_idx = {}
        union_find = UnionFind(len(accounts))
        for i, accnt in enumerate(accounts):
            for e in accnt[1:]:
                if e in email_to_acc_idx:
                    union_find.union(i, email_to_acc_idx[e])
                else:
                    email_to_acc_idx[e] = i
        
        merge_acc = collections.defaultdict(list)
        for e, i in email_to_acc_idx.items():
            leader = union_find.find(i)
            merge_acc[leader].append(e)

        result = []
        for i, email in merge_acc.items():
            name = accounts[i][0]
            result.append([name] + sorted(merge_acc[i]))

        return result