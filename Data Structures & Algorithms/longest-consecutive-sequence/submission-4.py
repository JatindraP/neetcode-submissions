class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = list(set(nums))
        num_set.sort()
        max_length = 1
        current_length = 1
        print(num_set)
        for i in range(len(num_set)-1):
            if num_set[i] + 1 == num_set[i+1]:
                current_length += 1
            else:
                max_length = max(max_length,current_length)
                current_length = 1
        max_length = max(max_length,current_length)
        return max_length
