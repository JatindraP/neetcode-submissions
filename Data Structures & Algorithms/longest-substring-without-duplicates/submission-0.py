class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_length = 0
        length = 0
        already_found = set()
        while l < len(s) and r < len(s):
            if s[r] not in already_found:
                already_found.add(s[r])
                length += 1
                r += 1
            else:
                already_found.remove(s[l])
                length -= 1
                l += 1
            max_length = max(max_length,length)
        return max_length

        