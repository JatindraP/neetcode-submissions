class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0]*26
        s2_count = [0]*26
        w_len = len(s1)
        for ch in s1:
            s1_count[ord(ch)-ord("a")] += 1
        i = 0
        j = w_len - 1
        while j < len(s2):
            if i == 0:
                s3 = s2[i:j+1]
                for ch in s3:
                    s2_count[ord(ch)-ord("a")] += 1
            else:
                s2_count[ord(s2[j])-ord("a")] += 1
                s2_count[ord(s2[i-1])-ord("a")] -= 1
            j += 1
            i +=1
            if s1_count == s2_count:
                return True
        return False
        