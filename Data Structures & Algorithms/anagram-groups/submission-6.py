class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for w in strs:
            w_k = ''.join(sorted(w))
            value = anagram_groups.get(w_k,[])
            value.append(w)
            anagram_groups[w_k] = value
        return [v for v in anagram_groups.values()]

        