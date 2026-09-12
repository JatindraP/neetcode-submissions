class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        nums_s = sorted(nums)
        i,j=0,len(nums_s)-1
        while i < j:
            current_sum = nums_s[i]+nums_s[j]
            if current_sum < k:
                max_sum = max(max_sum,current_sum)
                i+=1
            else:
                j-=1
        return max_sum
        