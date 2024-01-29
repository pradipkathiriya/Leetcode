class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        group_a = set()
        group_b = set()

        def dfs(i, prev_group):
            if prev_group == "A":
                if i in group_a:
                    return False
                if i in group_b:
                    return True
            if prev_group == "B":
                if i in group_b:
                    return False
                if i in group_a:
                    return True
            if prev_group == "A":
                curr_group = "B"
                group_b.add(i)
            else:
                curr_group = "A"
                group_a.add(i)
            
            for child in graph[i]:
                if not dfs(child, curr_group):
                    return False
            return True
        for i in range(len(graph)):
            if i in group_a or i in group_b:
                continue
            if not dfs(i, "B"):
                return False
        
        return True
