class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr) - 1:
                max_number = arr[i]
                arr[i] = -1
                continue
            new_max_number = max(max_number, arr[i])
            arr[i] = max_number
            max_number = new_max_number

        return arr
                 
        