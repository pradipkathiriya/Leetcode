class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        chache = {1 : 1}

        for num in range(2, n + 1):
            chache[num] = 0 if num == n else num
            for i in range(1, 1 + num//2):
                val = chache[i] * chache[num - i]
                chache[num] = max(chache[num], val)

        return chache[n]