class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in char_map:
                l = max(char_map[s[r]] + 1, l)
            
            char_map[s[r]] = r
            if (r - l + 1) > res:
                res = r - l + 1
        return res

