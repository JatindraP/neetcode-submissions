class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0

        for num in nums:
            length = 0
            if (num-1) not in nums:
                next_i = num
                while next_i in nums:
                    length+=1
                    next_i+=1
            max_length = max(max_length,length)
        return max_length

        