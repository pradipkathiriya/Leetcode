
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        curr_length = 0
        for char_s in s:
            if char_s == " ":
                curr_length = 0
                continue
            curr_length += 1
            res = curr_length

        return res 