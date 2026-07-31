class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_l = [0]*26
        t_l = [0]*26
        for ch in s:
            s_l[ord(ch)-ord('a')] += 1
        for ch in t:
            t_l[ord(ch)-ord('a')] += 1
        return s_l == t_l