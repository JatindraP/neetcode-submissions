class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one,one = 0,0
        for i in nums:
            if i == 0:
                max_one = max(max_one,one)
                one = 0
            else:
                one+=1
        max_one = max(max_one,one)
        return max_one
        