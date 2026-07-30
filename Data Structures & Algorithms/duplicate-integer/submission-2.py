class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        find = []
        for num in nums:
            if num in find:
                return True
            else:
                find.append(num)
        return False
        