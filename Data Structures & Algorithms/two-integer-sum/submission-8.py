class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in find:
                return [find.get(rem),i]
            else:
                find[nums[i]] = i

        