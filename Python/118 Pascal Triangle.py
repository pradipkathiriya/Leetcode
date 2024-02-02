class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]

        for i in range(numRows - 1):

            temp = [0] + res[-1] + [0]
            curr_row = [0] * (len(res[-1]) + 1)
            for j in range(len(temp) - 1):
                curr_row[j] = temp[j] + temp[j + 1]
            res.append(curr_row)

        return res
