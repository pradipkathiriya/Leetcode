class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}

        len_lis, res = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            max_len, max_count = 1, 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > max_len:
                        max_len = length + 1
                        max_count = count
                    elif length + 1 == max_len:
                        max_count += count
            if max_len > len_lis:
                len_lis, res = max_len, max_count
            elif max_len == len_lis:
                res += max_count
            
            dp[i] = [max_len, max_count]


        return res
        