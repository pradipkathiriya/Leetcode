class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(matrix), len(matrix[0])
        
        max_col = []
        
        for j in range(col):
            max_element = matrix[0][j]
            for i in range(row):
                if matrix[i][j] > max_element:
                    max_element = matrix[i][j]
                    
            max_col.append(max_element)
            
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_col[j]
                    
        return matrix