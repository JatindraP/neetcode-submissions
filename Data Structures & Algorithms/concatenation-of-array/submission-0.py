class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0]*(length*2)
        for i in range(length):
            ans[i] = nums[i]
            ans[length+i] = nums[i]
        return ans
        