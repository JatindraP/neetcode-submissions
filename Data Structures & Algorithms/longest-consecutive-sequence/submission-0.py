class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_list = list(set(nums)) # Take the Uinque element
        num_list.sort() # Sort the element in assending order

        max_length = 0
        num_len = len(num_list)
        length = 1

        for i in range(num_len):
            if i == 0:
                length = 1

            else:
                if num_list[i] == num_list[i-1] + 1:
                    length +=1
                else:
                    max_length = max(max_length,length)
                    length = 1
            if i == num_len -1 :
                max_length = max(max_length,length)
        return max_length
        