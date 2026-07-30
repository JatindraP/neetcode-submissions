class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] = count_dict[num] + 1
            else:
                count_dict[num] = 1

        for val in count_dict.values():
            if val > 1:
                return True

        return False
        