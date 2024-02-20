class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i, n in enumerate(nums):
            if i == 0:
                curr_sum = nums[0]
                max_sum = curr_sum
                continue

            if curr_sum < 0:
                curr_sum = 0

            curr_sum += n

            max_sum = max(max_sum, curr_sum)


        return max_sum