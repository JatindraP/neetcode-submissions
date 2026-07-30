class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_grp = defaultdict(list)

        for str1 in strs:
            anagram_key = [0] * 26
            for ch in str1:
                anagram_key[ord(ch) - ord("a")] += 1
            anagram_grp[tuple(anagram_key)].append(str1)
        return [a for a in anagram_grp.values()]
        