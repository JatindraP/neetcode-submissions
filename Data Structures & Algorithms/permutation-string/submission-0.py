class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w_length = len(s1)
        for i in range(len(s2)-(w_length-1)):
            s3 = s2[i:(i+w_length)]
            if sorted(s1) == sorted(s3):
                return True
        return False
        