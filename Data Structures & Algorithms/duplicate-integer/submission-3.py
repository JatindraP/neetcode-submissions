class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        find = set()
        for num in nums:
            if num in find:
                return True
            else:
                find.add(num)
        return False
        