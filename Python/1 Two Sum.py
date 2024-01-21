
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_map:
                return [i, nums_map[diff]]
            nums_map[nums[i]] = i
        