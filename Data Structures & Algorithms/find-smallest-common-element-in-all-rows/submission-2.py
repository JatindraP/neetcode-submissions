class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n = (10**4)+1
        count = [0]*n
        for m in mat:
            for i in m:
                count[i] = count[i]+1
        for i,c in enumerate(count):
            if c == len(mat):
                return i
        return -1
        