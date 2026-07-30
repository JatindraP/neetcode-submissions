class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        frd_prd = []
        bkrd_prd = []
        rev_nums = nums[::-1]
        fprd = 1
        bprd = 1
        for i in range(0,len(nums)):
            frd_prd.append(fprd)
            fprd*=nums[i]
            bkrd_prd.append(bprd)
            bprd*=rev_nums[i]
        rev_bkrd_prd = bkrd_prd[::-1]
        for i in range(0,len(nums)):
            product_list.append(frd_prd[i]*rev_bkrd_prd[i])
        return product_list

