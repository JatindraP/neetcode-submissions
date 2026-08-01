class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        ans = [0]*n
        for i in range(n):
            ans[i] = prod
            prod = prod*nums[i]
        prod = 1
        for i in range(n-1,-1,-1):
            ans[i] = ans[i]*prod
            prod = prod*nums[i]
        return ans

