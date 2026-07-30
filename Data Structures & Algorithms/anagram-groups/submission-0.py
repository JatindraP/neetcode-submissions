class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(str1: str,str2: str) -> bool:
            if len(str1) != len(str2):
                return False
            count_s1,count_s2 = {},{}
            for i in range(len(str1)):
                count_s1[str1[i]] = 1 + count_s1.get(str1[i],0)
                count_s2[str2[i]] = 1 + count_s2.get(str2[i],0)
            return count_s1 == count_s2
        anagram_group = []
        while len(strs) > 0:
            anagram = strs[0]
            anagrams = []
            non_anagrams = []
            for item in strs:
                if is_anagram(anagram,item):
                    anagrams.append(item)
                else:
                    non_anagrams.append(item)
            anagram_group.append(anagrams)
            strs = non_anagrams
        return anagram_group

        