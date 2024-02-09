class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        nums = sorted(list(set(nums)))
         
        earn1, earn2 = 0, 0

        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]
            # can't use both curEarn and earn2
            if i > 0 and nums[i] - 1 == nums[i - 1]:
                tmp = earn2
                earn2 = max(earn1 + curEarn, earn2)
                earn1 = tmp 
            else:
                earn1 = earn2
                earn2 = earn2 + curEarn

        return earn2