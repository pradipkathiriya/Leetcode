class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = 0
        global_max = nums[0]
        curr_min = 0
        global_min = nums[0]

        total = 0

        for n in nums:
            if curr_max < 0:
                curr_max = 0
            if curr_min > 0:
                curr_min = 0

            curr_max += n
            curr_min += n
            total += n

            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)

        if global_max < 0:
            return global_max

        return max(global_max, total - global_min)