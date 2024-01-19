class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        prereq = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        visit = set()
        completed = set()

        result = []

        def dfs(i, result):
            if i in completed:
                return True, result
            if i in visit:
                return False, result
            visit.add(i)
            for req in prereq[i]:
                can_take, result = dfs(req, result)
                if not can_take:
                    return False, result
            visit.pop()
            result.append(i)
            completed.add(i)

            return True, result

        for crs in range(numCourses):
            can_take, result = dfs(crs, result)
            if not can_take:
                return []

        return result
            