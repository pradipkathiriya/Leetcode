class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        length = len(graph)

        safe_node = {}

        def dfs(i):
            if i in safe_node:
                return safe_node[i]
            safe_node[i] = False

            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe_node[i] = True
            return True

        result = []
        for i in range(length):
            if dfs(i):
                result.append(i)

        return result





        