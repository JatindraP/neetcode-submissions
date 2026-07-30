class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        prod = 1
        for num in nums:
            product_list.append(prod)
            prod *= num

        prod = 1

        for i in range(len(nums)-1,-1,-1):
            product_list[i] = product_list[i] * prod
            prod *= nums[i]

        return product_list

