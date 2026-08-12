class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_count = [0,0,0]
        for n in nums:
            color_count[n]+=1

        k = 0
        for i,c in enumerate(color_count):
            for j in range(c):
                nums[k] = i
                k+=1
        