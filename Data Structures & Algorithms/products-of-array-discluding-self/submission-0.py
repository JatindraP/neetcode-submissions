class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prd = []
        lprdarr = [1]*n
        rprdarr = [1]*n
        lprd,rprd = 1,1
        for i in range(n):
            lprdarr[i] = lprd
            lprd *= nums[i]
        for j in range(n-1,-1,-1):
            rprdarr[j] = rprd
            rprd *= nums[j]
        for k in range(n):
            prd.append(lprdarr[k]*rprdarr[k])
        return prd
        