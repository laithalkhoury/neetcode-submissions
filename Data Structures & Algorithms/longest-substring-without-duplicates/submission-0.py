class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = set()

        i = 0
        j = 0

        max_len_so_far = 0
        for ch in s:
            if ch not in window:
                j += 1
            else:
                k = i
                for m in range(k, j + 1):
                    i += 1
                    window.remove(s[m])
                    if s[m] == ch:
                        break
                j += 1
            window.add(ch)
            if (j - i) > max_len_so_far:
                max_len_so_far = (j - i)


        return max_len_so_far