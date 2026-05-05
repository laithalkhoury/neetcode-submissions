class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n = len(s)
        m = len(t)
        if m != n:
            return False
        
        s1 = "".join(sorted(t))
        s2 = "".join(sorted(s))

        return s1 == s2