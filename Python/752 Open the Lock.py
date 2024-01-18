class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        if "0000" in deadends:
            return -1

        def children(lock):
            result = []
            for i in range(4):
                digit = str((int(lock[i]) + 1 ) % 10)
                result.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                result.append(lock[:i] + digit + lock[i+1:])
            return result

        visited = set(deadends)
        q = collections.deque()
        q.append(["0000", 0])

        while q:
            lock, move = q.popleft()
            if lock == target:
                return move
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append([child, move + 1])
        
        return -1