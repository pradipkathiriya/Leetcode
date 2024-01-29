class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        prereq = {i:[] for i in range(numCourses)}

        for cor, req in prerequisites:
            prereq[cor].append(req)


        curr_visit = set()


        def dfs(i):
            if not prereq[i]:
                return True

            if i in curr_visit:
                return False

            curr_visit.add(i)
            for req in prereq[i]:
                if not dfs(req):
                    return False

            curr_visit.pop()

            prereq[i] = []

            return True

        for cor in range(numCourses):
            if not dfs(cor):
                return False

        return True
