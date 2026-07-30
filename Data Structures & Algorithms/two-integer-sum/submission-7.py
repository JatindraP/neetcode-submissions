class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for i in range(len(nums)):
            if nums[i] in num_index:
                num_index[nums[i]].append(i)
            else:
                num_index[nums[i]] = [i]

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in num_index:
                index =  num_index.get(rem)
                index.append(i)
                index_set = set(index)
                final_index_list = list(index_set)
                if len(final_index_list) == 1:
                    continue
                else:
                    return final_index_list

        