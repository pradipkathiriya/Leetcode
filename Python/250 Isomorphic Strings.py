class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        character_map_s = {}
        character_map_t = {}

        for i in range(len(s)):
            if s[i] in character_map_s and t[i] != character_map_s[s[i]]:
                return False
            if t[i] in character_map_t and s[i] != character_map_t[t[i]]:
                return False
            character_map_s[s[i]] = t[i]
            character_map_t[t[i]] = s[i]

        return True
