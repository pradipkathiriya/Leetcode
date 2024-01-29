class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        incoming = collections.defaultdict(list)

        for src, dst in edges:
            incoming[dst].append(src)
        result = []
        for i in range(n):
            if i not in incoming:
                result.append(i)

        return result