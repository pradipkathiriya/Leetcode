class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dp = [False, False, False]
        if nums[-1] == nums[-2]:
            dp[1] = True
        if len(nums) == 2:
            return dp[1]
        if nums[-1] == nums[-2] == nums[-3] or nums[-1] - 1 == nums[-2] == nums[-3] + 1:
            dp[0] = True

        for i in range(len(nums) - 4, -1, -1):
            curr_part = False
            if nums[i] == nums[i + 1]:
                curr_part = dp[1]

            if nums[i] == nums[i + 1] == nums[i + 2] or nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1:
                curr_part = curr_part or dp[2]
            dp[2] = dp[1]
            dp[1] = dp[0]
            dp[0] = curr_part
        return dp[0]