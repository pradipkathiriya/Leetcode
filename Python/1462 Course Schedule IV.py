class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        direct_prereq = {i : [] for i in range(numCourses)}
        for req, crs in prerequisites:
            direct_prereq[crs].append(req)
        indirect_prereq = {i : set() for i in range(numCourses)}

        def dfs(i):
            if not indirect_prereq[i]:
                for req in direct_prereq[i]:
                    indirect_prereq[i] |= dfs(req)

                indirect_prereq[i].add(i)

            return indirect_prereq[i]


        for i in range(numCourses):
            dfs(i)

        result = []

        for u, v in queries:
            result.append(u in indirect_prereq[v])

        return result